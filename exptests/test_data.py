from src.quantpytoolkit.data import fetch_dummy_data

def test_fetch_dummy_data():
    df = fetch_dummy_data("FAKE", "2025-01-01", "2025-01-05")
    assert len(df) == 5
    assert "Close" in df.columns
