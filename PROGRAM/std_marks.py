


def details():
    global name
    global clas
    name = input('Enter students Name: ')
    clas = input('Class              : ')
    marks()


def marks():
    global math
    global phy
    global chem
    global cs
    global eng
    try:
        print('-----Enter marks------')
        math = int(input('Maths     : '))
        phy  = int(input('Physics   : '))
        chem = int(input('Chemistry : '))
        cs   = int(input('Cs        : '))
        eng  = int(input('Eng       : '))
        calculation()
    except:
        print('marks shld be only in integers\nPls Try again!')
        marks()


def calculation():
    global total_marks
    global percent
    global grade
    global status

    total_marks = math+phy+chem+cs+eng
    percent     = total_marks*100/500
    #percent
    if percent >= 95:
        grade = 'A+'
    elif percent >=90:
        grade = 'A'
    elif percent >=80:
        grade = 'B'
    elif percent >= 65:
        grade = 'C'
    elif percent >=50:
        grade = 'D'
    elif percent >= 35:
        grade = 'E'
    else:
        grade = 'F'
    #PASS OR FAIL
    if grade=='F':
        status = 'FAIL'
    else:
        status='PASS'
    output()
    

def output():
    print('*'*50)
    print('NAME  :',name.upper())
    print('CLASS :',clas.upper())
    print('*'*50)
    print('='*50)
    print('Marks')
    print('-'*50)
    print('MATHS     :',math)
    print('PHYSICS   :',phy)
    print('CHEMISTRY :',chem)
    print('CS        :',cs)
    print('ENGLISH   :',eng)
    print('-'*50)
    print('TOTAL MARKS =',total_marks,'/500')
    print('PERCENT     =',percent,'%')
    print('GRADE       =',grade)
    print('STATUS      =',status)
    print('='*50)

details()