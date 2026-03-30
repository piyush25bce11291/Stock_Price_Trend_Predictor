import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol="AAPL", start="2020-01-01", end="2024-01-01"):
    data = yf.download(symbol, start=start, end=end)
    data.reset_index(inplace=True)
    return data

if __name__ == "__main__":
    df = fetch_stock_data()
    print(df.head())