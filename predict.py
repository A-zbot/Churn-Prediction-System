import pickle
import pandas as pd

def load_model(
    model_path
):
    with open(
        model_path, 
        "rb"
        ) as file:

        model = pickle.load(
            file
            )

    return model

def predict_customer(
            model, 
            customer_data
):
    customer_df = pd.DataFrame(
        [customer_data]
    )

    prediction = model.predict(
        customer_df
    )[0]
    probability = (
        model.predict_proba(
        customer_df
    )[0][1]
    )
    

    return (
        prediction
        probability
    )

