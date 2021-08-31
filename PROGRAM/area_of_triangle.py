def area_by_base_height():
    base = int(input('Enter base of triangle'))
    height = int(input('Enter height of triangle'))
    print('Area of triangle is',(1/2)*base*height)

def area_by_sides(): #herons formula
    a = int(input('side 1 = '))
    b = int(input('side 2 = '))
    c = int(input('side 3 = '))

    semi_perimeter = (a+b+c)/2

    area = (semi_perimeter*(semi_perimeter-a)*(semi_perimeter - b)*(semi_perimeter - c))**0.5
    print('Area of triangle is ',area)
    if area == 0:
        print('Triangle cant be formed by these sides\nTry Again!!')
        area_by_sides()
    
