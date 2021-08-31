#asigning values
a = 10
b = 20

#adding
print(a+b)  #gives sum of a and b
#subracting 
print(a-b)  
#multiplication
print(a*b)

#Adding strings
a = 'Python'
b = 'Programming'
#add
print(a+b)   # gives = 'PythonProgramming')
print(a+'isa'+b+'language')  #gives = 'PythonisaPrograminglanguage

#num = '0 1 2 3 4 5'
#str = 'a b c d e f'
str = 'abcdefghijklmnopqrstuvwxyz'
print(str[0]) #gives = 'a'
print(str[5]) #gives = 'f'
#print(str[30]) #Error coz index value of 30 dont xist  #index error


#negative indexing
#num = '-6 -5  -4 -3 -2 -1'
#str = ' a  b   c  d  e  f'
str = 'abcdefghijklmnopqrstuvwxyz'
print(str[-1]) #gives 'z'

#print set of values
print(str[0:2])  #prints str[0] and str[1] #doesnt include last value
print(str[3:])   #prints str[2] to last charecter of string
print(str[:4])   #prints from start to 3rd charector


#strings in python are immutable(cant be changed once asigned)
#str[2] = 'C'  #gibes error

#Alternativ
str = 'YOUTUBE'
print('MY'+str[3:]) #gibes = 'MYTUBE'

#lenght of a string
print(len[str])