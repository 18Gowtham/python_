#PROGRAM TO ADD ALL THE ELEMENTS IN A LIST USING RECURSION

def Sum(List, N):
     if len(List)== 1:
        return List[0]
     else:
        return List[0]+ Sum(List[1:], N)
 

List =[]
no = int(input('Enter no of elements in list : '))
for i in range(no):
    element = int(input('=>'))
    List.append(element)


N = len(List)
result = Sum(List,N)
print(result)
