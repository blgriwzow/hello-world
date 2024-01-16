#This document serves as a sample program that emonstrates some Python basics
# Author: blgriwzow

while True:
  print('Hellow world!')
  print('What is your name, user?')
  username = input()
  
  if 'brittany' in username.lower():
    print('Hey, that\'s my name too!')
  elif 'harry' in username.lower():
    print('Yer a wizard, ' + username + '!')
  else:
    print('Greetings, earthling.')

  print('Would another user like to tell me their name? Enter \'yes\' to continue')
  answer = input()
  if answer.lower() != 'yes':
    print('Processing ending... ')
    break
    
print('That\'s all, folks!')

