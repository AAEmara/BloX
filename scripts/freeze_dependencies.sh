#!/usr/bin/bash

# Feeze python project dependencies
sudo docker compose exec web pip freeze > requirements.txt
