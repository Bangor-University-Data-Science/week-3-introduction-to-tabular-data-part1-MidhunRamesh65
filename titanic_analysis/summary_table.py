import pandas as pd

def create_summary_table(df: pd.DataFrame):
    """
    Creates a summary DataFrame with feature name, data type, number of unique values,
    and if it has missing values.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        pd.DataFrame: A summary DataFrame.
    """
    summary = {
        'Feature Name': df.columns,
        'Data Type': [df[col].dtype for col in df.columns],
        'Number of Unique Values': [df[col].nunique() for col in df.columns],
        'Has Missing Values?': [df[col].isnull().any() for col in df.columns]
    }
    
    return pd.DataFrame(summary)

# Example DataFrame
data = {
    'Age': [22, 38, 26, 35, None],
    'Sex': ['male', 'female', 'female', 'male', 'male'],
    'Survived': [0, 1, 1, 0, 1]
}
mock_df = pd.DataFrame(data)

# Creating the summary table
summary_df = create_summary_table(mock_df)
print(summary_df)

