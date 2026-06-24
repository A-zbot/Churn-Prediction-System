import pickle
import os

def save_model(
    model, 
    filepath
    ):

    os.makedirs(
        os.path.dirname(filepath),
        exist_ok=True
    )   

    with open(
        filepath, 
        'wb') as file:

        pickle.dump(
            model, 
            file)

        print(f"Model saved to {filepath}")