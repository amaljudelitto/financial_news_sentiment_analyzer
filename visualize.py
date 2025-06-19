import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_trend(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="date", y="sentiment_score", hue="ticker", marker="o")
    plt.title("Sentiment Trend Over Time")
    plt.ylabel("Sentiment Score")
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("sentiment_trend.png")
    plt.show()
