#dictionary
#first element = key
#second element= value
data = {1:'a',2:'b'}
#keys shld not be identical
#two values cant hv a same key

print(data[1]) #give = a

#print(data[3]) #gives an error
 
data.get(3)#gives = None

data.get(3,'Not found') #if there is no value for 3 it gives = not found

data.clear() # will clear the entire dict

keys = [1,2,3,4,5]
values = ['a','b','c','d','e']

data = dict(zip(keys,values))
print(data)
#joins both the dictionaries

#adding values
data[6] = 'f'

#delete dictionaries
del data[1] #removes 1 and 'a'

#we can crate a list in dictionary and a dictionary in dictionary

