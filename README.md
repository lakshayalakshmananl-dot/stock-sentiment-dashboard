# 📈 Stock Sentiment Dashboard

An AI-powered financial news analysis dashboard that uses **Retrieval-Augmented Generation (RAG)** to analyze stock-related news and generate an explainable market sentiment signal.

## 🚀 Project Overview

The Stock Sentiment Dashboard collects financial news and stock price data for a selected stock ticker.

The financial news is converted into vector embeddings and stored in a **FAISS vector index**. Relevant news is retrieved based on the stock's financial context and provided to a Large Language Model through the **Groq API**.

The system generates:

- Current stock price
- 1-month stock price chart
- Relevant financial news
- Overall sentiment
- Bullish / Bearish / Neutral signal
- AI-generated reasoning

The goal is to provide a **source-grounded and explainable stock sentiment analysis system**.

---

## 🧠 How It Works

```text
Stock Ticker
     ↓
Stock Price & Financial News Collection
     ↓
News Preprocessing
     ↓
Text Embeddings
     ↓
FAISS Vector Database
     ↓
Relevant News Retrieval
     ↓
RAG Context
     ↓
Large Language Model
     ↓
Sentiment + Signal + Reason
     ↓
Streamlit Dashboard


🛠️ Technologies Used
Python
Streamlit
Yahoo Finance / yfinance
Sentence Transformers
FAISS
Groq API
OpenAI GPT-OSS 120B
Pandas

Pandas
🔎 RAG Pipeline

1. News Collection
      Financial news is collected based on the selected stock ticker.

2. Embedding Generation
    News headlines are converted into numerical vector representations using a Sentence Transformer model.

3. Vector Storage
    The generated embeddings are stored in a FAISS vector index.

4. Retrieval
    FAISS retrieves the most relevant news headlines based on the financial query.

5. LLM Analysis

    The retrieved headlines are passed to **OpenAI GPT-OSS 120B through the Groq API** for sentiment analysis and signal generation.

6. Signal Generation
    The model analyzes the retrieved financial context and generates:

    Positive / Negative / Neutral sentiment
    Bullish / Bearish / Neutral signal
    Short explanation

📊 Dashboard Output

For a selected stock, the dashboard displays:

    Current stock price
    Historical price chart
    Relevant financial headlines
    AI-generated sentiment
    Market signal
    Explanation for the signal
