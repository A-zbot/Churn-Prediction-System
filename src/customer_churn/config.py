import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "customer.csv")
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "model.pkl")

RANDOM_STATE = 42
TEST_SIZE = 0.20
