from config import (
    DATA_PATH,
    MODEL_PATH
)

from load_data import load_data
from preprocess import preprocess_data
from feature_engineering import create_features
from eda import (
    plot_churn_distribution,
    plot_correlation_heatmap
)
from train import train_model
from evaluate import evaluate_model
from save_model import save_model

def main():
    print ("\nLoading Dataset..")
    df = load_data(DATA_PATH)
    print ("\nPreprocessing Dataset..")
    df = preprocess_data(df)
    print ("\nPreprocessing Completed..")
    print("\nFeature Engineering..")
    df = create_features(df)
    print ("\nGenerating EDA Plots..")
    plot_churn_distribution(df) 
    plot_correlation_heatmap(df)
    print ("\nTraining Model..")
    (
        model,
        x_train,
        x_test,
        y_train,
        y_test
    ) = train_model(df)
    evaluate_model(
        model, 
        x_test, 
        y_test
    )
 
    save_model(
        model, 
        MODEL_PATH
    )

if __name__ == "__main__":
    main()
    