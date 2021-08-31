#ROLLING DICE
import random 


print('DICE GAME')
o = True
while o is True:
    print('The number u got is',random.randint(1,6))
    choice = input('If want to stop program type (n)')
    if choice=='n'or 'N':
        print('Program ended!')
        o = False
    else:
        o = True


