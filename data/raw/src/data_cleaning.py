import pandas as pd


def clean_data(df):
    """
    Perform basic cleaning and data preparation.
    """

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Convert date column
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    # Remove rows with invalid dates
    df = df.dropna(subset=["Date"])

    # Create time features
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month Name"] = df["Date"].dt.month_name()
    df["Quarter"] = "Q" + df["Date"].dt.quarter.astype(str)

    # Create age groups
    age_bins = [0, 18, 25, 35, 45, 55, 65, 100]

    age_labels = [
        "Under 18",
        "18-24",
        "25-34",
        "35-44",
        "45-54",
        "55-64",
        "65+"
    ]

    df["Age Group"] = pd.cut(
        df["Age"],
        bins=age_bins,
        labels=age_labels,
        right=False
    )

    return df
