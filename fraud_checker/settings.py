import os

THRESHOLD = float(os.getenv('CLF_THRESHOLD', 0.5))
MODEL_PATH = os.getenv('MODEL_PATH', None)
