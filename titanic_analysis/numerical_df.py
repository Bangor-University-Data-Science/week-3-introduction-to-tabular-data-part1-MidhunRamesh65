import pandas as pd

def get_numerical_df(df: pd.DataFrame, numerical_features: list) -> pd.DataFrame:
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    return df[numerical_features]

# Example DataFrame
data = {
    'Age': [22, 38, 26, 35],
    'Fare': [7.25, 71.83, 7.92, 53.10],
    'Survived': [0, 1, 1, 0]
}
df = pd.DataFrame(data)

# Extracting numerical features
numerical_df = get_numerical_df(df, ['Age', 'Fare'])
print(numerical_df)


