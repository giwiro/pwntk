#!/usr/bin/env bash

export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

sudo "PATH=$PATH" pipenv run python ./main.py "$@"