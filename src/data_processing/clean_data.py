import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input dataframe by filling missing values with 0.
    """
    df = df.fillna(0)
    return df
