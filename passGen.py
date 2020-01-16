####################################
# Random Password Generator
####################################
from string import ascii_letters, digits
from random import choice

SYMBOL = '!?'

userInput = input('Which size do you want the password to have?\n>>> ')
userInput = int(userInput)

passw = ''.join([choice(ascii_letters + digits + SYMBOL)
                 for i in range(userInput)])

print('Your new pass is:\n')
print(passw)
