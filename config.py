import os

BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "data", "customer.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")

RANDOM_STATE = 42
TEST_SIZE = 0.20
