def calculate_descriptive_statistics(df):
    """
    Calculate descriptive statistics for numerical variables.
    """

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    statistics = df[numeric_columns].agg(
        ["mean", "median", "std"]
    ).T

    statistics["mode"] = [
        df[column].mode().iloc[0]
        if not df[column].mode().empty
        else None
        for column in numeric_columns
    ]

    return statistics


def monthly_sales(df):
    """
    Calculate monthly sales.
    """

    return (
        df.groupby(
            df["Date"].dt.to_period("M")
        )["Total Amount"]
        .sum()
        .sort_index()
    )


def quarterly_sales(df):
    """
    Calculate quarterly sales.
    """

    return (
        df.groupby(
            [df["Date"].dt.year,
             df["Date"].dt.quarter]
        )["Total Amount"]
        .sum()
        .reset_index()
    )


def category_revenue(df):
    """
    Calculate revenue by product category.
    """

    return (
        df.groupby("Product Category")["Total Amount"]
        .sum()
        .sort_values(ascending=False)
    )
