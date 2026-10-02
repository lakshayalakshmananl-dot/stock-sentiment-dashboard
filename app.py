import streamlit as st
import yfinance as yf

from news import get_news
from rag import create_embeddings, create_faiss_index, search_faiss
from llm import analyze_news


# --------------------------------------------------
# Page title
# --------------------------------------------------

st.title("📈 Stock Sentiment Dashboard")

st.write(
    "AI-powered stock sentiment analysis using financial news, "
    "FAISS retrieval, and a Large Language Model."
)


# --------------------------------------------------
# Stock input
# --------------------------------------------------

ticker_symbol = st.text_input(
    "Enter Stock Ticker",
    "AAPL"
).upper()


# --------------------------------------------------
# Analyze button
# --------------------------------------------------

if st.button("Analyze Stock"):

    # --------------------------------------------------
    # Step 1: Get stock price data
    # --------------------------------------------------

    stock = yf.Ticker(ticker_symbol)
    data = stock.history(period="1mo")

    if data.empty:
        st.error("Invalid stock ticker.")
        st.stop()

    current_price = data["Close"].iloc[-1]

    st.subheader(f"📊 {ticker_symbol} Stock")

    st.metric(
        "Current Price",
        f"${current_price:.2f}"
    )

    st.line_chart(data["Close"])


    # --------------------------------------------------
    # Step 2: Get financial news
    # --------------------------------------------------

    headlines = get_news(ticker_symbol)

    if not headlines:
        st.error("No news found for this stock.")
        st.stop()


    # --------------------------------------------------
    # Step 3: Create embeddings
    # --------------------------------------------------

    embeddings = create_embeddings(headlines)


    # --------------------------------------------------
    # Step 4: Create FAISS vector index
    # --------------------------------------------------

    index = create_faiss_index(embeddings)


    # --------------------------------------------------
    # Step 5: Retrieve relevant news
    # --------------------------------------------------

    query = f"{ticker_symbol} financial performance and stock outlook"

    results = search_faiss(
        query,
        index,
        headlines,
        top_k=min(3, len(headlines))
    )

    relevant_headlines = [
        result[0]
        for result in results
    ]


    # --------------------------------------------------
    # Step 6: Send retrieved news to LLM
    # --------------------------------------------------

    analysis = analyze_news(relevant_headlines)


    # --------------------------------------------------
    # Step 7: Display relevant news
    # --------------------------------------------------

    st.subheader("📰 Relevant News")

    for i, headline in enumerate(relevant_headlines, start=1):

        st.write(
            f"**{i}.** {headline}"
        )


    # --------------------------------------------------
    # Step 8: Display AI analysis
    # --------------------------------------------------

    st.subheader("🤖 AI Analysis")


    # --------------------------------------------------
    # Determine signal
    # --------------------------------------------------

    if "Signal: Bullish" in analysis:

        signal = "🟢 BULLISH"
        signal_color = "#21c354"

    elif "Signal: Bearish" in analysis:

        signal = "🔴 BEARISH"
        signal_color = "#ff4b4b"

    else:

        signal = "⚪ NEUTRAL"
        signal_color = "#808080"


    # --------------------------------------------------
    # Signal highlight line
    # --------------------------------------------------

    st.markdown(
        f"""
        <div style="
            border-top: 4px solid {signal_color};
            padding-top: 12px;
            margin-top: 10px;
            margin-bottom: 15px;
        ">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"## {signal}"
    )


    # --------------------------------------------------
    # Extract sentiment and reason
    # --------------------------------------------------

    sentiment = "Unknown"
    reason = "No reason available."


    for line in analysis.split("\n"):

        line = line.strip()

        if line.startswith("Sentiment:"):

            sentiment = line.replace(
                "Sentiment:",
                ""
            ).strip()

        elif line.startswith("Reason:"):

            reason = line.replace(
                "Reason:",
                ""
            ).strip()


    # --------------------------------------------------
    # Display sentiment
    # --------------------------------------------------

    st.markdown("### Sentiment")

    st.write(sentiment)


    # --------------------------------------------------
    # Display reason
    # --------------------------------------------------

    st.markdown("### Reason")

    st.write(reason)


    # --------------------------------------------------
    # Footer information
    # --------------------------------------------------

    st.caption(
        "News is retrieved and processed using embeddings and "
        "FAISS before being analyzed by the LLM."
    )
   