import pandas as pd

def load_csv(path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path)

def clean_columns(df):
    """Standardize column names."""
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

def convert_dates(df, col):
    """Convert a column to datetime using mixed format parsing."""
    df[col] = pd.to_datetime(df[col], format="mixed")
    return df

def basic_summary(df):
    """Return basic descriptive statistics."""
    return df.describe()

