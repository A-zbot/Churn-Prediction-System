# Customer Churn Prediction

This project trains a machine learning model to predict whether a customer will churn based on telecom customer data.

## Project structure

- `data/` - Input dataset
- `src/customer_churn/` - Core source code
  - `main.py` - End-to-end training pipeline
  - `config.py` - Project settings and file paths
  - `load_data.py` - Dataset loading
  - `preprocess.py` - Data cleaning and encoding
  - `feature_engineering.py` - New features
  - `eda.py` - EDA plots
  - `train.py` - Model training
  - `evaluate.py` - Evaluation metrics
  - `save_model.py` - Model serialization
  - `predict.py` - Prediction helpers
- `models/` - Saved trained model
- `tests/` - Regression tests
- `notebooks/` - Optional exploratory notebooks

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install pandas scikit-learn matplotlib seaborn
   ```
3. Run the training pipeline:
   ```bash
   python src/customer_churn/main.py
   ```

## Output

The pipeline trains a logistic regression model and saves it to `models/model.pkl`.

## Notes

- The dataset is expected at `data/customer.csv`.
- You can extend the project by adding more features, experimenting with different models, or adding a web API for predictions.
