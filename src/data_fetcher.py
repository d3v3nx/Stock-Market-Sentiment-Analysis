import yfinance as yf
import pandas as pd
import requests

def fetch_stock_data(ticker, start, end):
    stock = yf.download(ticker, start=start, end=end, auto_adjust=False)
    stock.reset_index(inplace=True)
    stock.columns = stock.columns.get_level_values(0)
    return stock

def fetch_news(api_key, query, from_date, to_date):
    if not api_key:
        raise ValueError("NEWS_API_KEY is missing")
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "language": "en",
        "sortBy": "relevancy",
        "apiKey": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("status") != "ok":
        raise Exception(f"NewsAPI error: {data.get('message')}")

    articles = data.get("articles", [])

    news = [{
        "date": article["publishedAt"][:10],
        "headline": article["title"]
    } for article in articles]

    return pd.DataFrame(news)