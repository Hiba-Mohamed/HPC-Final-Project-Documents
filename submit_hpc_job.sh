#!/bin/bash
#SBATCH --job-name=habit_tracker
#SBATCH --output=habit_tracker_%j.out
#SBATCH --error=habit_tracker_%j.err
#SBATCH --time=03:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --partition=standard

module load python/3.9

# Create or activate virtual environment
if [ ! -d ~/venv_habittracker ]; then
    python -m venv ~/venv_habittracker
fi
source ~/venv_habittracker/bin/activate

pip install --upgrade pip
pip install asteval

python hMohamed.py
