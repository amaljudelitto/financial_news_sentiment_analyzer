import requests
import json
import os

def fetch_news(tickers):
    from datetime import datetime, timedelta
    API_KEY = "demo"  # Replace with real key if needed
    all_news = []

    for ticker in tickers:
        url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={API_KEY}&pageSize=10"
        res = requests.get(url)
        data = res.json()
        articles = data.get("articles", [])
        for article in articles:
            all_news.append({
                "ticker": ticker,
                "title": article["title"],
                "date": article["publishedAt"]
            })

    with open("data/sample_headlines.json", "w") as f:
        json.dump(all_news, f, indent=2)

    return all_news
