# This program asks the user to guess a number between 1 and 10.
import random
rr=random.randint(1,10)
print('Guess which number I am thinking of now. It is between 1 and 10.')
yourNumber=input()
if int(yourNumber)==rr:
    print('Congrats, you got it!')
elif int(yourNumber) < rr:
    print('Larger...guess again!')
elif int(yourNumber) > rr:
    print('Lower...guess again!')
yourNumber2=input()
if int(yourNumber2)==rr:
    print('Two tries and you got it. Congrats!')
else:
    print('Guess one last time!')
yourNumer3=input()
if int(yourNumer3)==rr:
    print('You got it afterall. Congrats!')
else:
    print('It seems that today is not your lucky day. Better luck next time.')






    



