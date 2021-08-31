import csv


with open('a.csv','w', newline='') as csv_file:
    content = csv.writer(csv_file)
    content.writerow([1, 'Lily', 17])

with open('a.csv','r') as some_file:
    a = csv.reader(some_file)
    for row in a:
        print(row[1])