#Check for vowels in a sentence and print them in stack(last in first out format)



def program():
    statement = input('Enter a sentence in which u need to check count of vowels:\n')
    vowels_list = []
    for i in statement:
        if i in 'AEIOUaeiou':
            vowels_list.append(i)
    for i in range(len(vowels_list)-1,-1,-1):
        print(vowels_list[i])
    


