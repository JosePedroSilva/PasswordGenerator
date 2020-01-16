####################################
# Random Password Generator
####################################
from string import ascii_letters, digits
from random import choice


passw = ''.join([choice(ascii_letters + digits) for i in range(32)])
