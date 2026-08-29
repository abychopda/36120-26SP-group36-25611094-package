"""Unit tests for group36_25611094_package.helpers.submission."""

from __future__ import annotations

import pandas as pd
import pytest

from group36_25611094_package.helpers import submission


def test_keeps_most_recent_season_per_player():
    result = submission.create_submission_file(
        pid=[1, 1, 2],
        year=[2010, 2012, 2011],
        predicted_probabilities=[0.1, 0.8, 0.4],
    )

    assert list(result.columns) == ["pid", "label"]
    assert not result["pid"].duplicated().any()
    # Player 1's 2012 season (prob 0.8) wins over 2010.
    assert result.loc[result["pid"] == 1, "label"].iloc[0] == 0.8


def test_probability_out_of_range_raises():
    with pytest.raises(ValueError):
        submission.create_submission_file(
            pid=[1],
            year=[2010],
            predicted_probabilities=[1.5],
        )


def test_writes_csv_when_output_path_given(tmp_path):
    path = tmp_path / "submission.csv"
    submission.create_submission_file(
        pid=[1, 2],
        year=[2010, 2011],
        predicted_probabilities=[0.2, 0.7],
        output_path=path,
    )

    assert path.exists()
    written = pd.read_csv(path)
    assert list(written.columns) == ["pid", "label"]
