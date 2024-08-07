import asyncio
import os
import tempfile
import threading
import time
import unittest
from contextlib import contextmanager
from pathlib import Path

from pydantic import ValidationError
from structlog import get_logger
from xdg import BaseDirectory

from psychopy_session_webserver.participants_registry import ParticipantRegistry
from psychopy_session_webserver.session import Session
from psychopy_session_webserver.types import Experiment, Participant
from psychopy_session_webserver.update_broadcaster import UpdateEvent

from tests.mock_session import build_mock_session


class SessionTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()

        self.sessionDir = Path(self.tempdir.name).joinpath("session")
        ParticipantRegistry._filepath = Path(self.tempdir.name).joinpath(
            "xdg_data_dir/participants.json"
        )
        os.makedirs(ParticipantRegistry._filepath.parent)

        self.psy_session = build_mock_session(self.sessionDir)

        os.makedirs(self.sessionDir)
        self.local_filepath("foo.psyexp").touch()

        self.session = Session(root=self.sessionDir, session=self.psy_session)

    def local_filepath(self, path):
        return self.sessionDir.joinpath(path)

    def tearDown(self):
        self.session.close()
        self.tempdir.cleanup()
        del self.session
        ParticipantRegistry._filepath = Path(
            BaseDirectory.save_data_path("psychopy_session_webserver")
        ).joinpath("participants.json")

    def test_existing_experiment_are_listed(self):
        self.assertIn("foo.psyexp", self.session.experiments)

        self.assertEqual(
            self.session.experiments["foo.psyexp"],
            Experiment(
                key="foo.psyexp",
                resources={"foo.png": False},
                parameters=["participant", "session"],
            ),
        )

    def test_experiment_list_updates(self):
        self.local_filepath("bar.psyexp").touch()
        time.sleep(0.02)
        self.assertIn("bar.psyexp", self.session.experiments)
        expected = Experiment(
            key="bar.psyexp",
            resources={
                "baz/bar.png": False,
                str(Path(self.tempdir.name).joinpath("absolute.png")): False,
            },
            parameters=["participant", "session", "rewards"],
        )
        got = self.session.experiments["bar.psyexp"]
        self.assertEqual(expected, got, msg=f"expected: {expected}, got: {got}")

    def test_validity_updates(self):
        self.assertFalse(self.session._resourceChecker.collections["foo.psyexp"].valid)
        self.local_filepath("foo.png").touch()
        time.sleep(0.02)
        self.assertTrue(self.session._resourceChecker.collections["foo.psyexp"].valid)
        os.remove(self.local_filepath("foo.png"))
        time.sleep(0.02)
        self.assertFalse(self.session._resourceChecker.collections["foo.psyexp"].valid)

    @contextmanager
    def with_file(self, path):
        path = self.local_filepath(path)
        path.touch()
        time.sleep(0.02)
        yield
        os.remove(path)
        time.sleep(0.02)

    def test_run_experiment_asserts_required_parameters(self):
        with self.assertRaises(RuntimeError) as e:
            self.session.runExperiment("foo.psyexp")

        self.assertRegex(str(e.exception), "missing required parameter\\(s\\) \\[.*\\]")

    def test_run_experiment_asserts_missing_parameters(self):
        with self.assertRaises(RuntimeError) as e:
            self.session.runExperiment(
                "foo.psyexp",
                participant="Lolo",
                session=2,
                rewards=5,
            )

        self.assertRegex(
            str(e.exception), "invalid experiment parameter\\(s\\) \\['rewards'\\]"
        )

    def test_run_experiment_assert_resources(self):
        with self.assertRaises(RuntimeError) as e:
            self.session.runExperiment(
                "foo.psyexp",
                participant="Lolo",
                session=2,
            )

        self.assertEqual(
            str(e.exception),
            "experiment 'foo.psyexp' is missing the resource(s) ['foo.png']",
        )

    def test_run_experiment_validate_participant_name(self):
        with self.with_file("foo.png"), self.assertRaises(ValidationError) as e:
            self.session.runExperiment(
                "foo.psyexp",
                participant="some invalid name",
                session=3,
            )

        self.assertRegex(str(e.exception), "1 validation error for Participant")

    def test_run_experiment(self):
        with self.with_file("foo.png"):
            self.session.runExperiment(
                "foo.psyexp",
                participant="Lolo",
                session=2,
            )
        self.psy_session.runExperiment.assert_called_once_with(
            "foo.psyexp",
            {
                "participant": "Lolo",
                "session": 2,
                "date|hid": "foo",
                "psychopy_version|hid": "1.1.1",
            },
            blocking=True,
        )


class SessionEventTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.loop = asyncio.get_running_loop()

        self.tempdir = tempfile.TemporaryDirectory()

        ParticipantRegistry._filepath = Path(self.tempdir.name).joinpath(
            "xdg_data_dir/participants.json"
        )
        os.makedirs(ParticipantRegistry._filepath.parent)

        self.sessionDir = Path(self.tempdir.name).joinpath("session")

        os.makedirs(self.sessionDir)

        self.psy_session = build_mock_session(self.sessionDir)

        self.local_filepath("foo.psyexp").touch()

        self.session = Session(
            root=self.sessionDir, session=self.psy_session, loop=self.loop
        )
        self.updates = self.session.updates()

        event = await anext(self.updates)
        self.assertEqual(event.type, "catalogUpdate")
        self.assertDictEqual(
            event.data,
            {
                "foo.psyexp": Experiment(
                    key="foo.psyexp",
                    parameters=["participant", "session"],
                    resources={"foo.png": False},
                )
            },
        )
        event = await anext(self.updates)
        self.assertEqual(UpdateEvent(type="experimentUpdate", data=""), event)

        event = await anext(self.updates)
        self.assertEqual("participantsUpdate", event.type)

        event = await anext(self.updates)
        self.assertEqual(UpdateEvent(type="windowUpdate", data=False), event)

    async def asyncTearDown(self) -> None:
        self.session.close()
        self.tempdir.cleanup()
        ParticipantRegistry._filepath = Path(
            BaseDirectory.save_data_path("psychopy_session_webserver")
        ).joinpath("participants.json")

    def local_filepath(self, path):
        return self.sessionDir.joinpath(path)

    async def test_catalog_updates(self):

        self.local_filepath("foo.png").touch()
        event = await anext(self.updates)
        self.assertEqual(event.type, "catalogUpdate")
        self.assertDictEqual(
            event.data,
            {
                "foo.psyexp": Experiment(
                    key="foo.psyexp",
                    parameters=["participant", "session"],
                    resources={"foo.png": True},
                )
            },
        )

        os.remove(self.local_filepath("foo.psyexp"))
        event = await anext(self.updates)
        self.assertEqual(event.type, "catalogUpdate")
        self.assertDictEqual({"foo.psyexp": None}, event.data)

    async def test_experiment_update(self):
        self.local_filepath("foo.png").touch()
        event = await anext(self.updates)
        self.assertEqual(event.type, "catalogUpdate")

        self.session.runExperiment(
            "foo.psyexp",
            participant="Lolo",
            session=2,
        )

        event = await anext(self.updates)
        self.assertEqual(event.type, "participantsUpdate")
        self.assertEqual(event.data, {"Lolo": Participant(name="Lolo", nextSession=3)})

        event = await anext(self.updates)
        self.assertEqual(event.type, "windowUpdate")
        self.assertEqual(event.data, True)

        event = await anext(self.updates)
        self.assertEqual(event.type, "experimentUpdate")
        self.assertEqual(event.data, "foo.psyexp")

        event = await anext(self.updates)
        self.assertEqual(event.type, "experimentUpdate")
        self.assertEqual(event.data, "")

        self.session.closeWindow()
        event = await anext(self.updates)
        self.assertEqual(event.type, "windowUpdate")
        self.assertEqual(event.data, False)

    @contextmanager
    def with_file(self, path):
        path = self.local_filepath(path)
        path.touch()
        time.sleep(0.02)
        yield
        os.remove(path)
        time.sleep(0.02)

    @contextmanager
    def with_loop(self):
        thread = threading.Thread(target=self.session.run)
        thread.start()
        try:
            yield
        finally:
            self.session.close()
            thread.join()

    async def test_run_experiment_assert_none_running(self):
        with self.with_file("foo.png"), self.with_loop():
            await self.session.asyncRunExperiment(
                "foo.psyexp",
                participant="Lolo",
                session=2,
            )
            with self.assertRaises(RuntimeError) as e:
                await self.session.asyncRunExperiment(
                    "foo.psyexp",
                    participant="Lolo",
                    session=3,
                )
        self.assertEqual(str(e.exception), "experiment 'foo.psyexp' is already running")
