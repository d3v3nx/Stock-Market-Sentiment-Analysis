from dotenv import load_dotenv
import os
from src.data_fetcher import fetch_stock_data, fetch_news
from src.sentiment import add_sentiment_scores
from src.features import merge_stock_sentiment
from src.model import train_model

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

stock_df = fetch_stock_data("AAPL", "2025-12-01", "2025-12-20")
news_df = fetch_news(API_KEY, "Apple stock", "2025-12-01", "2025-12-20")

sentiment_df = add_sentiment_scores(news_df)
merged_df = merge_stock_sentiment(stock_df, sentiment_df)

model, accuracy = train_model(merged_df)
print(f"Model Accuracy: {accuracy:.2f}")