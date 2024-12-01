column1 = []
column2 = []
f = open("input.txt")

file = f.read()
file_list = file.splitlines()

for x in file_list:
    a, b = x.split()
    column1.append(a)
    column2.append(b)

column1.sort()
column2.sort()

column =[]


int_column1 = list(map(int,column1))
int_column2 = list(map(int,column2))

for x in range(1000):
    if(int_column1[x] > int_column2[x]):
        column.append(int_column1[x]-int_column2[x])
    elif(int_column2[x]>int_column1[x]):
        column.append(int_column2[x]-int_column1[x])
    else:
        column.append(0)


print(sum(column))
    

