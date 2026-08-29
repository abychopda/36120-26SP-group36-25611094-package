"""Unit tests for group36_25611094_package.helpers.cleaning."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from group36_25611094_package.helpers import cleaning


class TestHeightToInches:
    def test_feet_inches_format(self):
        result = cleaning.height_to_inches(pd.Series(["6-7"]))
        assert result.iloc[0] == 79

    def test_apostrophe_format(self):
        result = cleaning.height_to_inches(pd.Series(["6'4"]))
        assert result.iloc[0] == 76

    def test_month_name_format(self):
        # "6-Jul" is Excel's mangling of "6-7".
        result = cleaning.height_to_inches(pd.Series(["6-Jul"]))
        assert result.iloc[0] == 79

    def test_invalid_and_out_of_range_become_nan(self):
        result = cleaning.height_to_inches(pd.Series(["not-a-height", "20-3", None]))
        assert result.isna().all()

    def test_output_is_named(self):
        result = cleaning.height_to_inches(pd.Series(["6-0"]))
        assert result.name == "height_inches"


class TestRemoveFeatures:
    def test_drops_listed_columns(self):
        df = pd.DataFrame({"a": [1], "b": [2], "c": [3]})
        result = cleaning.remove_features(df, ["b"])
        assert list(result.columns) == ["a", "c"]

    def test_original_unchanged(self):
        df = pd.DataFrame({"a": [1], "b": [2]})
        cleaning.remove_features(df, ["b"])
        assert list(df.columns) == ["a", "b"]

    def test_unknown_columns_ignored(self):
        df = pd.DataFrame({"a": [1]})
        result = cleaning.remove_features(df, ["does_not_exist"])
        assert list(result.columns) == ["a"]

    def test_non_list_raises_type_error(self):
        df = pd.DataFrame({"a": [1]})
        with pytest.raises(TypeError):
            cleaning.remove_features(df, "a")

    def test_non_string_entries_raise_type_error(self):
        df = pd.DataFrame({"a": [1]})
        with pytest.raises(TypeError):
            cleaning.remove_features(df, ["a", 1])


class TestCalculateAge:
    def test_basic_age(self):
        dob = pd.Series(["1990-01-01", "1985-06-15"])
        season_year = pd.Series([2015, 2015])
        result = cleaning.calculate_age(dob, season_year)
        assert list(result) == [25, 30]

    def test_length_mismatch_raises_value_error(self):
        with pytest.raises(ValueError):
            cleaning.calculate_age(pd.Series(["1990-01-01"]), pd.Series([2015, 2016]))

    def test_invalid_dob_becomes_nan(self):
        result = cleaning.calculate_age(pd.Series(["nonsense"]), pd.Series([2015]))
        assert np.isnan(result.iloc[0])
