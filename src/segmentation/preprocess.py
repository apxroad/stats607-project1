from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def standardize(df: pd.DataFrame) -> tuple[pd.DataFrame, StandardScaler]:
    """
    Keep numeric columns and standardize them to ~N(0,1).

    Returns
    -------
    X_std : pd.DataFrame
        Standardized numeric features, same index/column names.
    scaler : StandardScaler
        Fitted scaler for inverse-transform/deployment.

    Raises
    ------
    ValueError
        If there are no numeric columns.
    """
    num = df.select_dtypes(include=[np.number])
    if num.shape[1] == 0:
        raise ValueError("No numeric columns to standardize")

    scaler = StandardScaler()
    X = scaler.fit_transform(num.values)
    X_std = pd.DataFrame(X, columns=num.columns, index=df.index)
    return X_std, scaler
