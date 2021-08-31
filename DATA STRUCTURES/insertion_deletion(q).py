'''
Write a function in python, INSERT(Arr,Data) and DELETE(Arr) for performing 
insertion and deletion operation in a queue. Arr is the list used for 
implementing queue and data is the value to be inserted.
'''

Arr = []
def insert():
    a = input('Enter data to be added: ')
    Arr.append(a)
   
def delete():
    if Arr == []:
        print('The list is already empty!')
    else:
        print('The first element of que is deleted\nThe poped element is',Arr[0])
        del Arr[0]

def program():
    choice = int(input('Choose!\n1.To add an element\n2.Remove an element\n3.Exit\n=>'))
    if choice == 1:
        a = int(input('Enter how many elements to be added : '))
        for i in range(a):
            insert()
        print('Elements added sucessfully!')
        print('Final list is : ',Arr)
        program()
    elif choice == 2:
        delete()
        program()
    else:
        print('Program ended')

program()