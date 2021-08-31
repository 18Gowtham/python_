#List manupulation
#lists are mutable


num = []  #Empty list 

#lists can contain integers,float,variables and other data types

list = [1,2,3,4,5]

#printing particular elements of list
print(list[0])
print(list[1])

#print set of elements of a list
print(list[2:]) #prints frm second index to last
print(list[:4]) #prints frm first index to 3rd index

#print can contain int and string value in a same list
list = [1,2,'apple']

#combining 2 lists
lis1 = [1,2,3]
lis2 = ['a','b','c']
list = [lis1 , lis2] #gives = [[1,2,3],['a','b','c']]

#adding an element to a list
list = [1,2,3]
list.append(4)
print(list)  #gives[1,2,3,4]

#adding element in particular index value
list.insert(2,5)
print(list)

#delete a number by value
list.remove(5)
print(list)

#delete based on index value
list.pop(1)   #removes element of index value 1

#to remove las element of list
list.pop()

#to remove a set of values
list = ['a','b','c','d','e','f','g']
del list[4:]   #deletes all elements frm list whose index value is above 4

#extend a set of elements to the list
list.extend([1,2,3,4])

#printing maximum and minimum value of list
list = [20,30,10,50,654,345]
min(list)
max(list)




