'''
Write a Program to implement book details using Stack.
'''
#stack  = Last in first out

list_final = [1,2,3] 

def add():
    for i in range(int(input('no of books : '))):
        book_name = input('Enter book name: ')
        author_name = input('Enter author name: ')
        list_1 = [book_name,author_name]
        list_final.append(list_1)
    print('Entered books are : ')
    for i in range(len(list_final)-1,-1,-1):
        print(list_final[i])

def remove():
    if len(list_final) == 0:
        print('List is empty')
    else:
        print('Last element popped out')
        print('Poped element is ',list_final.pop())
        print('Remaining elements in list are : ')
        for i in range(len(list_final)-1,-1,-1):
            print(list_final[i])

remove()