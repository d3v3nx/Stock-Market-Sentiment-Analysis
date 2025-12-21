import streamlit as st
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

from src.data_fetcher import fetch_stock_data, fetch_news
from src.sentiment import add_sentiment_scores
from src.features import merge_stock_sentiment
from src.model import train_model
from src.visualize import plot_sentiment_vs_price

# Load API key
load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

st.set_page_config(page_title="Stock Sentiment Analyzer", layout="wide")

st.title("📈 Stock Market Sentiment Analysis & Trend Prediction")

st.markdown(
    "Analyze how **news sentiment** impacts stock prices and predict short-term trends."
)

# ---------------- UI INPUTS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input("Stock Ticker", value="AAPL")

with col2:
    start_date = st.date_input(
        "Start Date", datetime.today() - timedelta(days=25)
    )

with col3:
    end_date = st.date_input(
        "End Date", datetime.today() - timedelta(days=1)
    )

# ---------------- RUN ANALYSIS ----------------
if st.button("🔍 Analyze & Predict"):
    with st.spinner("Fetching data and running model..."):
        try:
            stock_df = fetch_stock_data(
                ticker, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")
            )

            news_df = fetch_news(
                API_KEY,
                f"{ticker} stock",
                start_date.strftime("%Y-%m-%d"),
                end_date.strftime("%Y-%m-%d")
            )

            sentiment_df = add_sentiment_scores(news_df)
            merged_df = merge_stock_sentiment(stock_df, sentiment_df)

            model, accuracy = train_model(merged_df)

            st.success("Analysis completed successfully!")

            st.metric("📊 Model Accuracy", f"{accuracy:.2f}")

            latest_prediction = (
                "📈 UP" if model.predict(merged_df[["sentiment", "returns"]].iloc[[-1]])[0] == 1 else "📉 DOWN"
            )

            st.subheader("📌 Next-Day Trend Prediction")
            st.write(latest_prediction)

            st.subheader("📉 Sentiment vs Stock Price")
            st.pyplot(plot_sentiment_vs_price(merged_df))

        except Exception as e:
            st.error(f"Error occurred: {e}")
