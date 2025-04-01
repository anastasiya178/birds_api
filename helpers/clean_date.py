import pandas as pd


def clean_date(value):
    """ Clean date to avoid date format inconsistency and consequentual errors """

    dt = pd.to_datetime(value, errors='coerce')  # Convert to datetime safely
    # Detect non-missing values for an array-like object.
    if pd.notna(dt):
        return dt.strftime('%Y-%m-%d')  # Always return YYYY-MM-DD format
    return None  # Handle unparseable values
