#LINEAR SEARCH 

def linear_search(list, target):
    
    for i in range(0,len(list)):
        if i == target:
            return i
        
    return None


def verify(index):
    if index is not None:
        print('Index Found!',index)
    else :
        print('Target not found!')

numbers = [1,2,3,4,5]

result = linear_search(numbers,3)
verify(result)

