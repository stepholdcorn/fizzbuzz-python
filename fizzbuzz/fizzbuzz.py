def is_divisible_by_three(number):
  if number % 3 == 0:
    return 'Fizz'
  else:
    return number

def is_divisible_by_five(number):
  if number % 5 == 0:
    return 'Buzz'
  else:
    return number

def is_divisible_by_three_and_five(number):
  if number % 3 == 0 & number % 5 == 0:
    return 'Fizzbuzz'
  else:
    return number