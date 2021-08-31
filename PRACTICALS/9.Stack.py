#stack manupulation

List = []
def CREATING_STACK():
    no = int(input('Enter no of elements to be added in Stack'))
    for i in range(no):
        element = input('Enter the elemrent')
        List.append(element)
    print('Process finished')
    menu_driven()


def PUSH():
    element = input('Enter element to be added : ')
    List.append(element)
    print('Done!')
    menu_driven()

def dele():
    if List == []:
        print('There is nothing in the list!')
        menu_driven()
    else:
        print('Element poped out of the list is',List.pop())
    menu_driven()


def menu_driven():
    choice=int(input("1-CREATE 2-PUSH 3-POP 4-VIEW 5-EXIT\n=>"))
    if choice==1:
        print (" CREATING STACK")
        List = []
        CREATING_STACK()
    elif choice==2:
        print (" PERFORMING INSERTION")
        PUSH()
    elif choice==3:
        print (" PERFORMING DELETE")
        dele()
    elif choice==4:
        print ("CONTENT ARE:")
        print(List)
        menu_driven()

menu_driven()



