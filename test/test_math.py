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
