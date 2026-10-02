import yfinance as yf

def get_news(ticker_symbol):
    search = yf.Search(ticker_symbol)
    news = search.news

    headlines = []

    for article in news:
        # New Yahoo format
        if "content" in article:
            title = article["content"].get("title")

        # Older/simple format
        else:
            title = article.get("title")

        if title:
            headlines.append(title)

    return headlines