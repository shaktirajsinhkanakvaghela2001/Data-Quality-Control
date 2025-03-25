import pandas as pd

def profile_data(df):
    profile = {
        'completeness': df.isnull().mean(),
        'uniqueness': df.nunique(),
        'value_distribution': {col: df[col].value_counts(normalize=True) for col in df}
    }
    return profile