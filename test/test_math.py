import pytest

"""
This module contains basic unit test for math operations.
Their pourpose is to show how to use the pytest framework by expample.
"""


# ----------------------------------------------------------------------------------------
# A most basic test function
# ----------------------------------------------------------------------------------------

def test_one_plus_one():
	assert 1 + 1 == 2


# ----------------------------------------------------------------------------------------
# A test function to show assertion introspection
# ----------------------------------------------------------------------------------------

def test_one_plus_two():
	a = 1
	b = 2
	c = 3
	assert a + b == c


# ----------------------------------------------------------------------------------------
# A test function that verifies and exception
# ----------------------------------------------------------------------------------------

def test_divide_by_zero():
	with pytest.raises(ZeroDivisionError) as e:
		num = 1 / 0
	assert 'division by zero' in str(e.value)
