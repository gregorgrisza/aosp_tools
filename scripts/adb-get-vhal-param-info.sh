#!/bin/bash

adb root && adb shell dumpsys android.hardware.automotive.vehicle.IVehicle/default --get $1
