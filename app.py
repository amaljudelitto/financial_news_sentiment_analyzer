from news_scraper import fetch_news
from sentiment_analysis import analyze_sentiment
from visualize import plot_sentiment_trend

if __name__ == "__main__":
    tickers = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]
    headlines = fetch_news(tickers)
    sentiment_df = analyze_sentiment(headlines)
    plot_sentiment_trend(sentiment_df)
