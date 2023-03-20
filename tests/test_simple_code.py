import os
import sys

import numpy as np
import numpy.testing as npt
import pandas.testing as pdt
import pytest

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from simple_code import (
    stupid_yes,
    transform_features,
    represantive_random_sample
)

def test_stupid_yes_correct_output():
    expected = "yes"
    returned = stupid_yes()

    assert expected == returned

def test_transform_features_correct_output_type():
    returned = transform_features(np.array([1, 2, 3]))

    assert isinstance(returned, np.ndarray)


@pytest.mark.parametrize(
    "a, a_transformed",
    [
        pytest.param(np.array([0, 0, 0]), np.array([1, 1, 1]), id="zeros"),
        pytest.param(np.array([1, 2, 3]), np.array([3, 5, 7]), id="default"),
        pytest.param(np.array([-1, 0, 1]), np.array([-1, 1, 3]), id="real numbers")
    ]
)
def test_transform_features_correct_transformation(a, a_transformed):
    returned = transform_features(a)
    npt.assert_allclose(returned, a_transformed)


def test_represantive_random_sample(reference_df):
    expected = reference_df.head(1)
    returned = represantive_random_sample(reference_df)
    pdt.assert_frame_equal(expected, returned)
