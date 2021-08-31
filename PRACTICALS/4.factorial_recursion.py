#PROGRAM TO FIND FACTORIAL OF A GIVEN NUMBER USING RECURSION

def recur(n):
    if n == 1:
        return 1
    else:
        return n*recur(n-1)
    


def program():
    no = int(input('Enter a positive number to find its factorial : '))
    if no<0:
        print('Factorial of negative number cant be found!!\nTry again!!')
        program()
    elif no == 0:
        print('Factorial of 0 is 1')
        cont()
    else:
        print('Factorial of',no,'is',recur(no))
        cont()
    
def cont():
    choice = input('Want to continue(y/n) ?')
    if choice == 'y':
        print('Choosed to continue!')
        program()
    else:
        print('Program ended')


program()

        

     