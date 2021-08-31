#To write a Python program to print contents of a data file line by line

file = open(r'd:\COMPUTER SCIENCE\PRACTICALS\6.read.txt','r')
str = ' '

while str:
    str = file.readline()
    print(str,end='')

file.close()



