#!/bin/bash
# entrypoint.sh

# Exit script if any command fails
set -e

# Run your fill_data_set.py script
python src/fill_data_set.py

# After fill_data_set.py has completed, run main.py
python main.py