import pandas as pd
from quantpytoolkit.analytics import compute_returns, compute_volatility

def test_compute_returns_and_volatility():
    prices = pd.DataFrame({"Close": [100, 101, 102, 104]})
    returns = compute_returns(prices)
    vol = compute_volatility(returns)
    assert len(returns) == 3
    assert vol >= 0
