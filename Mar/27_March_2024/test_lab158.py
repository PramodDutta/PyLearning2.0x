# Fixture ( Concept in python) , pytest
# You can use the Fixture 1. setup, provide, teardown resource in your Testcases.
import pytest


# pass some of the data to other testcases you can use the fixture.


@pytest.fixture
def sample_data():
    data = [1, 2, 3, 4, 5]  # type -> list
    return data

@pytest.fixture
def sameple_data2():
    return True


def test_number1_sample_data_to_injected(sample_data):
    assert len(sample_data) == 5
    
def test_2(sample_data,sameple_data2):
    assert sameple_data2 == True
    assert 3 in sample_data
