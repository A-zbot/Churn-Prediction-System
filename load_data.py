import pandas as pd
def load_data(path: str = "data/customer.csv"):
    df = pd.read_csv("data/customer.csv")
    return df
    


    