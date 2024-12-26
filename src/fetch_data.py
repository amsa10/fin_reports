import yfinance as yf

def fetch_shale_oil_data(tickers):
    shale_data = {}
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            history = stock.history(period="5d")
            if history.empty:
                raise ValueError(f"No data available for {ticker}")
            current_price = history["Close"][-1]
            price_change = (history["Close"][-1] - history["Close"][0]) / history["Close"][0] * 100
            shale_data[ticker] = {
                "ticker": ticker,
                "current_price": current_price,
                "price_change": price_change
            }
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return shale_data
