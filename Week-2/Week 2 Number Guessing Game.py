# This program asks the user to guess a number between 1 and 10.
import random
print('Guess which number I am thinking of now. It is between 1 and 10.')
yourNumber=input()
print(int(yourNumber)==random.randint(1,10))
