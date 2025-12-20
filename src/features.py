import pandas as pd

def merge_stock_sentiment(stock_df, sentiment_df):
    stock_df["Date"] = stock_df["Date"].astype(str)
    merged = pd.merge(
        stock_df,
        sentiment_df,
        left_on="Date",
        right_on="date",
        how="left"
    )
    merged["sentiment"] = merged["sentiment"].fillna(0)
    merged["returns"] = merged["Close"].pct_change()
    return merged.dropna()
