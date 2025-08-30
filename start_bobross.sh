#!/bin/bash

# Bob Ross - A Happy Little Player Startup Script

# Set working directory
cd ~/bob-ross-player

# Activate virtual environment if you use one (optional)
# source venv/bin/activate

# Start the player and log output
nohup python3 bobross_player.py > ~/bobross.log 2>&1 &

echo "Bob Ross - A Happy Little Player started. Log: ~/bobross.log"
