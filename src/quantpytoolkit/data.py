import pandas as pd
import datetime as dt

def fetch_dummy_data(symbol: str, start: str, end: str) -> pd.DataFrame:

    dates = pd.date_range(start=start, end=end)
    prices = (100 + pd.Series(range(len(dates))) * 0.5).tolist()
    return pd.DataFrame({"Date": dates, "Close": prices}).set_index("Date")
