def remove_duplicates(df, key_columns):
    return df.drop_duplicates(subset=key_columns)

def standardize_format(df, column, format_function):
    df[column] = df[column].apply(format_function)
    return df