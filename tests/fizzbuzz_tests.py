from nose.tools import *
from fizzbuzz import fizzbuzz

def test_is_divisible_by_three():
  assert_equal(fizzbuzz.is_divisible_by_three(3), 'Fizz')