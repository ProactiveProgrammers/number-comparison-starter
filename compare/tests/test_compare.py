"""Test suite to ensure that each function works correctly."""

from compare import __version__

from compare import main

# TODO: Make sure that you read and understand all of the test cases inside of
# this test suite. You should be able to identify the following parts of a test:
# --> function under test
# --> input to the function under test
# --> output of the function under test
# --> assertion involved the output of the function under test and the test
# oracle (note that these are encoded in assert statements)


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_find_minimum():
    """Confirm that the function can find the minimum of three values."""
    minimum = main.get_minimum(3, 4, 5)
    assert minimum == 3
    minimum = main.get_minimum(5, 4, 3)
    assert minimum == 3
    minimum = main.get_minimum(4, 3, 5)
    assert minimum == 3


def test_largest_odd_can_find_one():
    """Confirm that it is possible to find the largest odd value when it exists."""
    (largest_odd, found) = main.get_largest_odd(21, 4, 17)
    assert largest_odd == 21
    assert found is True
    (largest_odd, found) = main.get_largest_odd(21, 4, 117)
    assert largest_odd == 117
    assert found is True


def test_largest_odd_cannot_find_one():
    """Confirm that it is possible to find the largest odd value when it does not exist."""
    (largest_odd, found) = main.get_largest_odd(20, 4, 18)
    assert largest_odd == 4
    assert found is False
    (largest_odd, found) = main.get_largest_odd(120, 400, 110)
    assert largest_odd == 110
    assert found is False
