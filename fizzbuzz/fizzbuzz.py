def is_divisible_by_three(number):
  return number % 3 == 0

def is_divisible_by_five(number):
  return number % 5 == 0

def is_divisible_by_three_and_five(number):
  return number % 3 == 0 and number % 5 == 0

def play(number):
  if is_divisible_by_three_and_five(number):
    return 'Fizzbuzz'
  elif is_divisible_by_three(number):
    return 'Fizz'
  elif is_divisible_by_five(number):
    return 'Buzz'
  else:
    return number