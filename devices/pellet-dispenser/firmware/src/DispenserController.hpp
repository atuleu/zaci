#pragma once

#include "Button.hpp"
#include "Error.hpp"
#include "PelletCounter.hpp"
#include "WheelController.hpp"
#include "hardware/DRV8848.hpp"
#include "pico/types.h"

class Mode;

class DispenserController : public Processor {
public:
	~DispenserController();

	struct StaticConfig {
		Button          &TestButton;
		IRSensor        &PelletSensor, &WheelSensor;
		PelletCounter   &Counter;
		WheelController &Wheel;
	};

	struct Config {
		uint MaxSlotRatio             = 12;
		int  ToggleDirectionThreshold = 10;
		uint MaxDirectionChange       = 6;
		uint PelletCounterCooldown_us = 1200 * 1000;
		uint SelfCheckPeriod_us       = 120 * 1000 * 1000;
	} __attribute__((packed));

	DispenserController(
	    const StaticConfig      &staticConfig,
	    const Config            &config,
	    WheelController::Config &wheelConfig
	);

	using DispenseCallback = std::function<void(uint, Error)>;

	void Dispense(
	    uint count, const DispenseCallback &callback = [](uint, Error) {}
	);

	struct CalibrationResult {
		uint Speed             = -1;
		uint MinRewindPulse_us = -1;
		uint Position          = -1;
	};

	using CalibrateCallback =
	    std::function<void(const CalibrationResult &, Error)>;

	void Calibrate(
	    uint                     speed,
	    const CalibrateCallback &callback = [](const CalibrationResult &,
	                                           Error) {}
	);

	void SetSpeedAndCalibrate(
	    uint speed, const std::function<void(Error)> &callback
	);

	void Process(absolute_time_t time) override;

private:
	friend class Mode;
	friend class IdleMode;
	friend class SelfCheckMode;
	friend class DispenseMode;
	friend class CalibrateMode;
	void processErrors();

	const Config            &d_config;
	WheelController::Config &d_wheelConfig;

	Button          &d_button;
	IRSensor        &d_wheelSensor, &d_pelletSensor;
	WheelController &d_wheel;
	PelletCounter   &d_counter;
	bool             d_sane = false;

	std::unique_ptr<Mode> d_mode;

	using Command = std::function<std::unique_ptr<Mode>()>;

	Queue<Command, 16, false> d_queue;
};
