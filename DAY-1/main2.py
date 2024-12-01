column1 = []
column2 = []
f = open("input.txt")

file = f.read()
file_list = file.splitlines()

for x in file_list:
    a, b = x.split()
    column1.append(a)
    column2.append(b)

int_column1 = list(map(int,column1))
int_column2 = list(map(int,column2))

column_1 = []

for x in range(6):
    count = 0 
    for y in range(6):
        if(int_column1[x]==int_column2[y]):
            count = count+1
    column_1.append(int_column1[x]*count)

column_2 =[]
for x in range(6):
    count = 0 
    for y in range(6):
        if(int_column2[x]==int_column1[y]):
            count = count+1
    column_2.append(int_column2[x]*count)
    
print(sum(column_1))
print(sum(column_2))
print(sum(column_1)+sum(column_2))