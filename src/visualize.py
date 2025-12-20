import matplotlib.pyplot as plt

def plot_sentiment_vs_price(df):
    fig, ax1 = plt.subplots()

    ax1.set_xlabel("Date")
    ax1.set_ylabel("Close Price")
    ax1.plot(df["Date"], df["Close"], label="Stock Price")

    ax2 = ax1.twinx()
    ax2.set_ylabel("Sentiment")
    ax2.plot(df["Date"], df["sentiment"], color="orange", label="Sentiment")

    plt.title("Stock Price vs News Sentiment")
    plt.show()
