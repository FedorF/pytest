import os

import pandas as pd
import pytest


PATH_TO_TEST_DATA = f"{os.path.dirname(os.path.abspath(__file__))}/test_data/sample.csv"


@pytest.fixture
def reference_df() -> pd.DataFrame:
    return pd.read_csv(PATH_TO_TEST_DATA)


@pytest.fixture
def reference_output() -> str:
    return "All good!"
