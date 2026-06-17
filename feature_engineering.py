import pandas as pd

def create_features(df:pd.DataFrame) ->pd.DataFrame:

    df = df.copy()

    df["ChargesPerMonth"] = (
        df["TotalCharges"] 
        /
        (df["tenure"] + 1)
    )

    df["IsNewCustomer"] = [
        df["tenure"] < 12
    ].astype(int)


    return df
 
    