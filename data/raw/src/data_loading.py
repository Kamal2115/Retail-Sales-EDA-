import pandas as pd


def load_data(file_path):
    """
    Load the retail sales dataset.
    """
    df = pd.read_csv(file_path)

    print(f"Dataset loaded successfully: {df.shape[0]} rows, "
          f"{df.shape[1]} columns")

    return df
