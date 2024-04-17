#pragma once

#include "DRV8848.hpp"
#include "PIOIRSensor.hpp"
#include "pico/time.h"
#include "pico/types.h"
#include <optional>
#include <tuple>

class WheelController {
public:
	const static int  RAMP_UP_DURATION_US    = 10000;
	const static int  RAMP_DOWN_DURATION_US  = 18000;
	const static uint SENSOR_LOWER_THRESHOLD = 160;
	const static uint SENSOR_UPPER_THRESHOLD = 220;
	const static int  MAX_STEP_TIME_US       = 500000;
	const static int  STEP_THRESHOLD         = 20;

	struct Config : public DRV8848::Config, public PIOIRSensor<1>::Config {
		uint SensorEnablePin;
		int  Speed = 200;
	};

	enum class Error {
		NO_ERROR = 0,
		BLOCKED  = 1,
	};

	WheelController(const Config &config);

	std::tuple<std::optional<int>, Error> Process(absolute_time_t time);

	int  Position();
	void Move(int wanted);
	void Stop();

private:
	enum class State {
		IDLE = 0,
		RAMPING_UP,
		MOVING_TO_TARGET,
		RAMPING_DOWN,
	};

	bool Stalled(absolute_time_t time) const;

	void SetIdle(absolute_time_t);
	void SetRampingUp(absolute_time_t time);
	void SetRampingDown(absolute_time_t time);
	void SetMoving(absolute_time_t time);

	bool ChangeDirection(absolute_time_t time);

	std::optional<int> ProcessSensor(absolute_time_t time);

	DRV8848        d_driver;
	PIOIRSensor<1> d_sensor;
	State          d_state = State::IDLE;
	int            d_speed;
	int            d_direction       = 1;
	bool           d_lastState       = false;
	int            d_directionChange = 0;

	int             d_position = -1, d_wanted = 0;
	absolute_time_t d_stateStart = nil_time;
	absolute_time_t d_lastStep   = nil_time;
};