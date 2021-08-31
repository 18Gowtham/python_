#PROGRAM TO REMOVE THE LINES THAT CONTAINS CHARACTER ‘A’

file_1 = open(r'd:\COMPUTER SCIENCE\PRACTICALS\7.readfile.txt','r')
file_2 = open(r'd:\COMPUTER SCIENCE\PRACTICALS\7.ritefile.txt','w')

for i in file_1:
    if 'a' not in i:
        file_2.write(i)
    
file_1.close()
file_2.close()

file_2 = open(r'd:\COMPUTER SCIENCE\PRACTICALS\7.ritefile.txt','r')
for i in file_2:
    print(i,end='')




