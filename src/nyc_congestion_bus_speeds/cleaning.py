def snake_case_columns(df):
    """Convert column names to snake_case."""
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df