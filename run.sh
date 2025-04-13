#!/bin/bash

# Kill any running Python processes
pkill -9 python3

# Wait a moment to ensure ports are freed
sleep 1

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
echo "Installing/updating dependencies..."
pip install -r requirements.txt

# Run the app
echo "Starting the application..."
python3 app.py
