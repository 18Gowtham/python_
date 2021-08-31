#Student register

def cont():
    choice = (input('Want to continue[Y/N]'))
    if choice == 'Y':
        print('Choosed to continue')
        Program()
    else :
        print('Program ended')



def Evaluate():
    print('_'*50)
    print('NAME  : ',lis[0])
    print('CLASS : ',lis[1])
    print('MARK1 : ',lis[2])
    print('MARK2 : ',lis[3])
    print('Total : ',lis[2]+lis[3])
    print('Avg   : ',(lis[2]+lis[3])/2)
    print('_'*50)
    cont()


def Program():
    global lis
    name = input('Enter Students Name')
    clas = int(input('Enter students class'))
    print('Marks')
    m1 = int(input('Enter sub1 Mark'))
    m2 = int(input('Enter sub2 Mark'))
    lis = []
    lis.append(name)
    lis.append(clas)
    lis.append(m1)
    lis.append(m2)
    Evaluate()

Program()





