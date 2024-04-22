while True:
  try:
    age = init(input('Please enter your age:'))
    10/age
  except ValueError:
    print('Please enter a number only')
  except ZeroDivisionError:
    print('Please enter a number higher than 0')
  else:
    print('Thank you')
    break
  finally:
    print('I am finally done')