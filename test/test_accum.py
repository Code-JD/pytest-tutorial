"""
This module contains basic unit tests for the accum module.
Their prupose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------------
# Imports
# --------------------------------------------------------------------------------------

import pytest
from stuff.accum import Accumulator


# --------------------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------------------

@pytest.fixture
def accum():
	return Accumulator()		# return/yield, yield turns it to a generator


# --------------------------------------------------------------------------------------
# Test
# --------------------------------------------------------------------------------------

def test_accumulator_init(accum):
	# accum = Accumulator()
	assert accum.count == 0


def test_accumulator_add_one(accum):
	# accum = Accumulator()
	accum.add()
	assert accum.count == 1


def test_accumulator_add_three(accum):
	# accum = Accumulator()
	accum.add(3)
	assert accum.count == 3


def test_accumulator_add_twice(accum):
	# accum = Accumulator()
	accum.add()
	accum.add()
	assert accum.count == 2


# def test_accumulator_cannot_set_count_directly(accum):
# 	# accum = Accumulator()
# 	with pytest.raises(AttributeError, match=r"can't set attribute") as #<WHAT??!?!?>
# 		accum.count = 10