import sys
import os
import pytest
import pandas as pd

# This block helps the test find the student's code in the main folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from analysis import calculate_average_score

def test_average_calculation():
    # We know the average of [85, 90, 78, 92, 88] is exactly 86.6
    result = calculate_average_score('data.csv')
    
    # Check if the result matches our expectation
    assert result == 86.6, f"Expected average 86.6, but got {result}"
    
    # Check if the return type is correct (it should be a float, not a string or None)
    assert isinstance(result, float), "The function should return a float value"

if __name__ == "__main__":
    pytest.main()