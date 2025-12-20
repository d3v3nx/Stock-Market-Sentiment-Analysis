from textblob import TextBlob

def get_sentiment(text):
    if not text:
        return 0
    return TextBlob(text).sentiment.polarity

def add_sentiment_scores(news_df):
    news_df["sentiment"] = news_df["headline"].apply(get_sentiment)
    daily_sentiment = news_df.groupby("date")["sentiment"].mean().reset_index()
    return daily_sentiment
