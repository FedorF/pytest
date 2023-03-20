import numpy as np
import pandas as pd


def stupid_yes() -> str:
    """Return 'yes' all the time.

    Returns:
        str: 'yes'
    """
    return "yes"


def transform_features(a: np.ndarray) -> np.ndarray:
    """Pretty difficult pipeline of feature transformations.

    Args:
        a (np.ndarray): initial data.

    Returns:
        np.ndarray: transformed data.
    """
    # slightly difficult code here
    a_transformed = a * 2 + 1

    return a_transformed


def represantive_random_sample(df: pd.DataFrame) -> pd.DataFrame:
    """Difficult logic for represantive sample from big pandas dataframe.

    Args:
        df (pd.DataFrame): big pandas dataframe.

    Returns:
        pd.DataFrame: small, but represantive sample.
    """
    return df.head(1)
