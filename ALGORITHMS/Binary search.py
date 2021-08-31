#BINARY SEARCH

def binary_search(list, target):
    first = list[0]
    last = len(list) - 1

    while first <= last:
        mid_point = (first+last)//2

        if list[mid_point]==target :
            return mid_point
        elif list[mid_point]<target:
            first = mid_point+1
        else:
            last = mid_point-1

    return None

def verify(index):
    if index is not None:
        print('Index Found!',index)
    else :
        print('Target not found!')

numbers = [1,2,3,4,5]

result = binary_search(numbers,3)
verify(result)
