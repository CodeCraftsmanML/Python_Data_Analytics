import pandas as pd
from src.data_processing.clean_data import clean_data

def test_clean_data():
    df = pd.DataFrame({'A': [1, None, 3]})
    cleaned = clean_data(df)
    assert cleaned.isnull().sum().sum() == 0

test_clean_data()
print("Test passed!")
