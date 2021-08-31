

#ax^2+bx+c   FORMAT
def quad():
    a = int(input('=>'))
    b = int(input('=>'))
    c = int(input('=>'))

    if a == 0:
        print('first no cant be zero in quadric equation\nTry Again!!')
        quad()
    else:
        discriminant = (b**2)- (4*a*c)
        root1 = (-b) + (discriminant)**0.5
        root2 = (-b) - (discriminant)**0.5
        if discriminant>0:
            print('Two real roots xists')
            print('Roots are ',root1,' , ',root2)
        elif discriminant<0:
            print('No real roots exist')
            print('Imaginary roots are',root1,' , ',root2)
        elif discriminant==0:
            print('One root xists')
            print('the root is',root1)

quad()
        
