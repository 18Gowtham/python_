#recursive search

def recurcive_search(list, target):
    if len(list)==0:
        return False
    else:
        midpoint = len(list)//2
        if target == list[midpoint]:
            return True
        else:
            if list[midpoint]<target:
                return recurcive_search(list[midpoint+1:], target)
            else:
                return recurcive_search(list[:midpoint], target)

def verify(index):
    print('Target found : ',index)

list = [1,2,7]
result = recurcive_search(list, 7)
verify(result)
