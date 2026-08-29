"""Shared pytest fixtures for the helper module test suite."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """A small frame with numeric + categorical columns, missing values and a duplicate row."""
    df = pd.DataFrame(
        {
            "age": [25, 30, 35, 40, np.nan],
            "points": [10.0, 20.0, 30.0, 40.0, 50.0],
            "position": ["G", "F", "G", "C", "F"],
            "team": ["A", "B", "A", "C", None],
        }
    )
    # Append an exact duplicate of the first row.
    return pd.concat([df, df.iloc[[0]]], ignore_index=True)


@pytest.fixture
def correlated_df() -> pd.DataFrame:
    """Two perfectly correlated numeric columns plus an unrelated one."""
    base = np.arange(1, 21, dtype=float)
    return pd.DataFrame(
        {
            "x": base,
            "x_scaled": base * 2.0 + 1.0,
            "noise": np.tile([1.0, -1.0], 10),
        }
    )
