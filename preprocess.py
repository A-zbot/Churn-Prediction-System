import pandas as pd
from load_data import load_data
from sklearn.preprocessing import LabelEncoder
def preprocess_data(df):
    df = df.copy()
    
    df = df.dropna('customerID', axis=1, inplace=True)
    df['TotalCharges'] = (
      df['TotalCharges'].replace(" ", 0)).astype(float)
    )

    df["Churn"] = (
        df["Churn"].map({
            "Yes": 1,
            "No": 0
        }) 
    )    

    encoder = LabelEncoder()

    catergorical_columns = [
        for col in df.columns
        if df[col].dtype == "object"
    ]   
    
    
    for column in categorical_columns:
        df[column] = encoder.fit_transform(
            df[column]

    
    )            

    return df
   