"""
Tests for molssi_math module
"""

import pytest
import numpy as np
import molssi_devops_uf as md_uf


@pytest.fixture(
    scope="function",
    params=[
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4., 5.],
        [1, "2", int(3), 4., 5.],
        [1, "20", int(13), 4., 5.],
        [21, "0", int(-13), 4., -5.],
    ]
)
def num_list(request):
    return request.param


@pytest.fixture
def num_list_and_mean(num_list):
    return (num_list, np.mean([float(num) for num in num_list]))


def test_mean(num_list_and_mean):
    num_list, expected = num_list_and_mean
    print("num_list:", num_list)
    observed = md_uf.mean(num_list)
    print("observed:", observed)
    print("expected:", expected)
    assert observed == expected

@pytest.mark.parametrize(
    "test_input",
    [
        'this is not a list',
        bool,
        None
    ]
)
def test_mean_wrong_type(test_input):
    with pytest.raises(TypeError):
        md_uf.mean(test_input)