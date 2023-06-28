"""
Test file
"""

import os
import sys
from unittest.mock import patch  # from mock import patch # older
import pytest
import json
from src.util.save_single_stock_info import save_single_stock_info
from src.util.save_single_stock_price_history import save_single_stock_price_history

def test_save_single_stock_info():
    """
    tests the behaviour of save_single_stock()
    """
    # Arrange
    test_path = os.path.realpath(
        os.path.join(
            os.path.dirname(__file__),
            "../output/individual_stock_data/2023-06-16/2023-06-16-AAPL-data.json",
        )
    )
    ticker = 'AAPL'
    AAPL_dict = json.loads(test_path)
    with patch(
        ["yq.Ticker()", "current_stock.all_modules", "json.dump(current_stock_data, stock_file, indent=4, sort_keys=False)"], 
        return_value = [True, AAPL_dict, True]
    ):
        save_single_stock_info(ticker)
        result = 
    # Assert
    assert 
