# settings.py
import os

# Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')
MODEL_DIR = os.path.join(os.path.dirname(__file__), '../models')
STATIC_DIR = os.path.join(os.path.dirname(__file__), '../static')

# Model Parameters
MODEL_PARAMS = {
    'learning_rate': 0.01,
    'epochs': 100,
    'batch_size': 32,
}

# Roulette Parameters
ROULETTE_NUMBERS = list(range(0, 37))  # European roulette has 37 pockets (0-36)
HOT_NUMBERS_THRESHOLD = 5  # Number of spins to consider a number 'hot'
