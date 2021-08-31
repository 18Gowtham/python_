#random
import random

#gives and random float number btwn 0 and 1
print(random.random())

#randint
print(random.randint(1,10)) #last element is not considered(here 10)

#randrange
print(random.randrange(0,100,10)) #100 is also included
#1st = starting
#2nd = ending
#3rd varing range


#shufling elements
a = [1,2,3,4,5]
random.shuffle(a) #shuffles the elements in a random way

#choice
#chooses 1 element frm set of elements
a = ['a','b','c','d']
random.choice(a)
