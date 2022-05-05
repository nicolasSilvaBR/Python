# For loop using Range

def prime_checker (number):
  is_prime = True
  for i in range(2,number):
    if number % i == 0:
      is_prime = False      
  if is_prime == True:
    print("Its a prime Number ")
  else:
    print("Its not a prime Number ")