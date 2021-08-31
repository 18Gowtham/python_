#importing
import os
from os import path
import time

#functions
def reading():
    try:
        file_1 = open(path2,'r')
        ask = int(input('1.Read entire file\n2.Read particular charectors\n3.Read particular line:\n=>'))
        print('*'*40)
        if ask==1:
            print(file_1.read())
            print('*'*40)
            print('Done!!')
        elif ask==2:
            a = int(input('Enter how many letters to read: '))
            print('#'*40)
            print(file_1.read(a))
            print('#'*40)
            print('Done!!')
        elif ask ==3:
            a = int(input('Enter no of lines to be printed: '))
            print('#'*40)
            for i in range(0,a):
                print(file_1.readline())
            print('#'*40)
            print('Done')
            
    except:
        print('Error \nTry again!!!')
        reading()
def Writing():
    a = input('Enter ur content: ')
    file_2 = open(path2,'w')
    file_2.write(a)
    file_2.close()
    print('Sucessfully wrote ur content in file')
def appen():
    file_3 = open(path2,'a')
    a = input('Enter content to be added: ')
    file_3.write(a)
    file_3.close()
    print('Succesfully added your content')
def dele():
    if path.exists(path2):
        os.remove(path2)
        print('file deleted')
    else:
        print('File not found')

#menu
def menu():
    try:
        print('*'*50)
        print('Choose\n1.Reading document\n2.Writing document(deletes already exixting content)\n3.Adding something to the file\n4.Deleting a file')
        print('*'*50)
        choice = int(input('=>'))
        if choice==1:
            print('Choosed to read the document')
            ('#'*40)
            reading()
            ('#'*40)
            start()
        elif choice==2:
            print('Choosed to write on a document')
            ('#'*40)
            Writing()
            ('#'*40)
            start()
        elif choice==3:
            print('Choosed to append')
            ('#'*40)
            appen()
            ('#'*40)
            start()
        elif choice==4:
            print('Choosed to delete file')
            ('#'*40)
            dele()
            ('#'*40)
            start()
        else:
            ('#'*40)
            print('Invalid input\nTry again!!!')
            ('#'*40)
            menu()
    except:
        print('Invalid input\nTry again!!!')
        menu()

#program start
def start():
    try:
        print('#'*50)
        ask = int(input('Choose\n1.Create new file\n2.edit existing file\n3.Exit\n=>'))
        print('#'*50)
        if ask==1:
            print('Choosed to create a file')
            create()
        elif ask==2:
            print('Choosed to edit a created file')
            edit()
        elif ask==3:
            end_()
        else:
            print('Invalid input\nTry again!\nprogram restarting')
            start()
    except:
        print('Invalid input\nTry again!\nprogram restarting')
        start()

#asking path
def path_way():
    global path1
    print('_'*50)
    path1 = input('Enter path of the folder\n=>')
    if path.exists(path1):
        print('Path exists')
        print('_'*50)
        start()
    else:
        print('!'*50)
        print('Invalid path\nTry again!!')
        print('!'*50)
        path_way()

#creating new file
def create():
    global path2
    try:
        def ask1():
            print('#'*40)
            ask = int(input('Choose\n1.Create another file\n2.Edit created file\n3.Edit existing file\n4.Exit program\n=>'))
            print('#'*40)
            if ask == 1:
                print('Choosed to create another file')
                print('#'*40)
                create()
            elif ask==2:
                print('choosed to edit created file')
                print('#'*40)
                menu()
            elif ask==3:
                edit()
            elif ask==4:
                end_()
            else:
                print('Invalid input\nEnter a valid input')
                print('#'*50)
                ask1()
        file_name = input('Enter name of file: ')
        path2 = path1+file_name+'.txt'
        file1 = open(path2,'x')
        print('Sucessfully created file')
        ask1()
    except ValueError:
        print('Invalid input\nEnter a valid input')
        print('#'*50)
        ask1()
    except FileExistsError:
        print('='*50)
        print('File already exists\nTry to choose another name')
        print('='*50)
        create()

#Editing existing file
def edit():
    global path2
    print('#'*40)
    print('Files on the directory are:')
    none = 0
    for a in os.listdir(path1):
        if a.endswith('.txt'):
            none=none+1
            print(none,'.',a)
    print('#'*40)
    file_name = input('Enter file name: ')
    path2 = path1+file_name+'.txt'
    if path.exists(path2):
        print('File found')
        print('#'*40)
        menu()
    else:
        print('No file named so..\Try again!!')
        edit()

#End 
def end_():
    print('%'*50)
    print('Program ended!\nThankyou')
    print('%'*50)
    time.sleep(5)

path_way()
