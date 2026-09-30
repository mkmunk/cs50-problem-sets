import pytest
import pandas as pd
from project import get_stock_data
from project import calculate_five_year_change
from project import display_stock_info


def test_get_stock_data():
    info, history = get_stock_data("AAPL")
    assert info["symbol"] == "AAPL"

    info, history = get_stock_data("NVDA")
    assert info["symbol"] == "NVDA"

    info, history = get_stock_data("MSFT")
    assert info["symbol"] == "MSFT"

    info, history = get_stock_data("GOOGL")
    assert info["symbol"] == "GOOGL"

def test_calculate_five_year_change():
    fake_history = pd.DataFrame({"Close": [100, 150]})
    result = calculate_five_year_change(fake_history)
    assert result == "50.00%"

    fake_history = pd.DataFrame({"Close": [50, 25]})
    result = calculate_five_year_change(fake_history)
    assert result == "-50.00%"

    fake_history = pd.DataFrame({"Close": [100, 20]})
    result = calculate_five_year_change(fake_history)
    assert result == "-80.00%"

def test_display_stock_info():
    fake_info = {
        "longName": "Auo Corporation",
        "sector": "Technology",
        "currentPrice": 50,
        "fiftyTwoWeekLow": 110,
        "fiftyTwoWeekHigh": 200,
        "marketCap": 150,
        "trailingPE": 20,
        "trailingEps": 2.5,
        "profitMargins": 0.50,
        "dividendYield": 0.03

    }

    result = display_stock_info(fake_info, "100%")

    assert "Auo Corporation" in result
    assert "Technology" in result
    assert "50" in result
    assert "110 - 200" in result
    assert "150" in result
    assert "20" in result
    assert "2.5" in result
    assert "0.5" in result
    assert "0.03" in result