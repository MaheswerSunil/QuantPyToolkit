import pandas as pd

def compute_returns(prices: pd.DataFrame) -> pd.Series:
    """Compute simple daily returns."""
    return prices["Close"].pct_change().dropna()

def compute_volatility(returns: pd.Series) -> float:
    """Return annualized volatility estimate."""
    return returns.std() * (252 ** 0.5)
