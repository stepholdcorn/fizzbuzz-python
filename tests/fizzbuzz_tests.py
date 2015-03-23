from nose.tools import *
from fizzbuzz import fizzbuzz

def test_is_divisible_by_three():
  assert_equal(fizzbuzz.is_divisible_by_three(3), 'Fizz')
  assert_equal(fizzbuzz.is_divisible_by_three(4), 4)

def test_is_divisible_by_five():
  assert_equal(fizzbuzz.is_divisible_by_five(5), 'Buzz')
  assert_equal(fizzbuzz.is_divisible_by_five(4), 4)