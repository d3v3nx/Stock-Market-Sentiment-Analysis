# Stock Market Sentiment Analysis & Trend Prediction

This project is an interactive analytical application that studies the relationship between **financial news sentiment** and **stock price movements**.  
It combines **NLP-based sentiment analysis**, **historical stock data**, and **machine learning** to explore whether news sentiment can help predict short-term market trends.

A user-facing web interface allows dynamic stock selection and date-based analysis, transforming the project from a static analysis into a usable analytical tool.

---

## 🚀 Live Demo
👉 https://portfolio.deven.co.in/Stock-Market-Sentiment-Analysis/

---

## 🔍 Key Features
- Fetches historical stock price data using Yahoo Finance  
- Collects financial news headlines via NewsAPI  
- Performs sentiment analysis on news using NLP techniques  
- Engineers sentiment and price-based features  
- Predicts next-day stock price direction using machine learning  
- Interactive **Streamlit UI** for dynamic user input and visualization  
- Cloud deployment with secure API key management  

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Data & ML:** Pandas, NumPy, Scikit-learn  
- **NLP:** TextBlob  
- **APIs:** Yahoo Finance, NewsAPI  
- **Visualization:** Matplotlib  
- **UI & Deployment:** Streamlit, Streamlit Cloud  

---

## 🧠 Methodology
1. Collect historical stock price data for a selected ticker  
2. Fetch corresponding financial news headlines for the same date range  
3. Apply sentiment analysis to news headlines and aggregate daily sentiment  
4. Merge sentiment data with stock price features such as returns  
5. Train a classification model to predict next-day price direction  
6. Visualize sentiment trends alongside stock price movements  

---

## 📈 Results & Insights
The project demonstrates how market sentiment can be incorporated as an analytical signal alongside price-based indicators.  
It also highlights the **noisy and uncertain nature of financial markets**, emphasizing realistic expectations from sentiment-driven models.

---

## ⚠️ Limitations
- NewsAPI free-tier restricts access to recent historical data  
- Stock prices are influenced by multiple external factors beyond news sentiment  
- The model is intended for analytical exploration, not trading execution  

---

## 🔮 Future Improvements
- Upgrade sentiment analysis using VADER or FinBERT  
- Add technical indicators (moving averages, RSI, volatility)  
- Extend support to multiple stocks and sectors  
- Improve model performance with advanced feature engineering  

---

## ⚠️ Disclaimer
This project is for **educational and analytical purposes only** and does not constitute financial or investment advice.
