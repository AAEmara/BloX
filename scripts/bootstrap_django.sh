#!/usr/bin/bash

# Bootstrap Django Project using a disposable container.
sudo docker run -it --rm \
  -v ${PWD}:/app \
  -w /app python:3.12-slim \
  bash -c "pip install django && django-admin startproject blox_app . && pip freeze > requirements.txt"
