import pandas as pd
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):
    df = df.copy()

    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce").fillna(0)

    if "Churn" not in df.columns:
        raise ValueError("Expected 'Churn' column in the dataset.")

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0}).astype(int)

    categorical_columns = [
        col
        for col in df.columns
        if col != "Churn" and (
            pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_string_dtype(df[col])
        )
    ]

    for column in categorical_columns:
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column].astype(str))

    return df
   