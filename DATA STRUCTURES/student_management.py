#Student management system using STACK (last in first out)

state = 'y'
final_list = []

while state == 'y':
    print('STUDENT DETAILS')
    name      = input('Name : ')
    clas      = int(input('Class :'))
    tot_marks = float(input('Marks : '))
    lis = [name,clas,tot_marks]
    final_list.append(lis)
    cont_status = input('Want to continue(y/n): ')
    if cont_status == 'n':
        state = 'n'
    else:
        state = 'y'

if state == 'n':
    ask = input('Want to print the result(y/n)? ')
    if ask == 'y':
        for i in range(len(final_list)-1, -1,-1):
            print(final_list[i])
    else:
        print('program ended')

