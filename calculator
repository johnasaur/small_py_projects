# write a basic calculator

from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {'+' : add, '-': subtract, '*': multiply,
              '/': divide }

# function = operations['*']

def calculator():

  num1 = float(input("what's the first number?: "))
  
  
  for o in operations:
    print(o)
  
  continued = True
  while continued:
    operations_symbol = input("pick operation symbol: ")
    num2 = float(input("what's the second number?: "))
    calculation_function = operations[operations_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    
    #  second calculation
    # operations_symbol = input("pick operation symbol from above: ")
    # num3 = int(input("what's the next number?: "))
    # calculation_function = operations[operations_symbol]
    # answer = calculation_function(calculation_function(num1, num2),num3)
  
    if input(f"type 'y' to continue calculating with {answer}, 'n' to exit: ") == 'y':
      num1 = answer
    else:
      continued = False
      calculator()

calculator()
  
