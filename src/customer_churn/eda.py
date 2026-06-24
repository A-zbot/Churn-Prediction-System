import matplotlib.pyplot as plt
import seaborn as sns


def plot_churn_distribution(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(x="Churn", data=df)
    plt.title("Customer Churn Distribution")
    plt.tight_layout()
    plt.show()


def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()