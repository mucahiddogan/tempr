#!/bin/bash

## echo function
echo_func () {
	printf "\n%b\n" "$1"
}

echo_func "Installing lm-sensors"
sudo apt-get install -y lm-sensors

echo_func "Installing notify-send"
sudo apt-get install -y notify-osd

