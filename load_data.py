import os
import pandas as pd


def load_data(path: str = None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__), "data", "customer.csv")
    return pd.read_csv(path)
    


    