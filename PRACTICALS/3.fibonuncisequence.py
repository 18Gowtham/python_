print('The Fibonacci sequence is a series of numbers where a number is \nthe addition of the last two numbers, starting with 0, and 1.')

# Python program to display the Fibonacci sequence

def fibo_recursion(n):
   if n <= 1:
       return n
   else:
       return(fibo_recursion(n-1) + fibo_recursion(n-2))

def program():
    number = int(input('Enter a number : '))
    if number<=0:
        print('Fibonacci series of negative num cant be fond!!\nTry again!!')
    else:
        print('FIBO SERIES : ')
        for i in range(number+1):
            print(fibo_recursion(i))

def cont():
    choice = input('Want to continue(y/n) ?')
    if choice == 'y':
        print('Choosed to continue!')
        program()
    else:
        print('Program ended')



program()
cont()




