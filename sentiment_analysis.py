import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(news):
    analyzer = SentimentIntensityAnalyzer()
    rows = []

    for article in news:
        score = analyzer.polarity_scores(article["title"])["compound"]
        rows.append({
            "ticker": article["ticker"],
            "date": article["date"][:10],
            "sentiment_score": score
        })

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df
