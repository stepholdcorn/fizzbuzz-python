from nose.tools import *
from fizzbuzz import fizzbuzz

def test_is_divisible_by_three():
  assert_equal(fizzbuzz.is_divisible_by_three(3), True)
  assert_equal(fizzbuzz.is_divisible_by_three(4), False)

def test_is_divisible_by_five():
  assert_equal(fizzbuzz.is_divisible_by_five(5), True)
  assert_equal(fizzbuzz.is_divisible_by_five(4), False)

def test_is_divisible_by_three_and_five():
  assert_equal(fizzbuzz.is_divisible_by_three_and_five(15), True)
  assert_equal(fizzbuzz.is_divisible_by_three_and_five(4), False)

def test_play():
  assert_equal(fizzbuzz.play(3), 'Fizz')
  assert_equal(fizzbuzz.play(5), 'Buzz')
  assert_equal(fizzbuzz.play(15), 'Fizzbuzz')
  assert_equal(fizzbuzz.play(4), 4)