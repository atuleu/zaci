#pragma once

#include "Controller.hpp"
#include "PelletCounter.hpp"
#include "WheelController.hpp"
#include "pico/types.h"

enum class OutputChannel {
	A             = 0,
	B             = 1,
	STEPPER_MOTOR = 2,
};

struct Config {
	WheelController::Config Wheel;
	PelletCounter::Config   Pellet;

	Controller::Config Main;
};
