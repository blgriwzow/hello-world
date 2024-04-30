'''

Basic low-level datatype validation using Python

basic validation structure:

# Priming read, collect the initial data
# Conditional loop, check for invalid data
  # Error message, alert the user to the issue
  # Recollect data from user to change conditional loop
# Return the good data once the conditional loop ends

Using Python's try/except to catch ValueErrors
Using Python's while True to keep the user trapped

'''

'''
Module to store the main program statements
'''
def main():
  int_response = get_integer('Please enter a whole number: ')
  float_response = get_float('Please enter a number: ')
  string_response = get_string('Please enter your favorite color: ')

  print()
  print('Thank you for playing!')

'''
Function to collect integer input from the user
'''
def get_integer(message):
  while True:
    try:
      input_int = int(input(message)) # attempts to convert user input to int, may cause a crash
      return input_int # returns good data if no crash occurs
    except ValueError:
      print('Error! Must enter a whole number.')

'''
Function to collect float input from the user
'''
def get_float(message):
  while True:
    try:
      input_float = float(input(message)) # attempts to convert user input to float, may cause a crash
      return input_float # returns good data if no crash occurs
    except ValueError: # catches crashes
      print('Error! Must enter a number.')

'''
Function to collect non-blank string input from the user
'''
def get_string(message):
  input_str = input(message) # priming read, collect the initial data
  while input_str.replace(' ', '') == '': # conditional loop, checks for blank input
    print('Error! Must enter a response.')
    input_str = input(message) # recollect data from the user
  return input_str # returns good data if the conditional loop ends

main() # call the main module to begin program execution
