matrix = []
#reading file and writing to matrix var
with open(r"C:\Users\Dell\Desktop\Coding\linalg.txt","r") as file:
    rows = int(file.readline())
    columns = int(file.readline())
    while True:
        record = file.readline()
        if record != "":
            record = list(map(float,record.split()))
            matrix.append(record)
        else:
            break

def piv():
    global matrix
    pivots = []
    for i in matrix:
        for j in i:
            if j != 0:
                pivots.append(i.index(j))
                break 
    return pivots   

def makeone():
    pivots = piv()
    for i in range(rows):
        try:
            pivot = matrix[i][pivots[i]]
            for j in range(columns):
                matrix[i][j] = matrix[i][j]/pivot
        except:
            continue

def subtract(a,b):
    for _ in range(len(a)):
        matrix[b][_] = matrix[b][_] - a[_]

pivot = 0
current_row = 0
while pivot < columns:
    if current_row >= rows:
        break
    for i in range(rows):
        if matrix[i][pivot] != 0:
            matrix[current_row], matrix[i] = matrix[i], matrix[current_row]
            for k in range(rows):
                if k != current_row:
                    makeone()
                    flag = 1
                    for j in range(columns):
                        if matrix[k][j] != 0:
                            pivotentry = j
                            flag = 0
                            break
                    if flag == 0:
                        factor = matrix[current_row][pivotentry]
                        vector = []
                        for j in range(len(matrix[0])):
                            vector.append(matrix[k][j]*factor)
                        subtract(vector,current_row)
            pivot += 1
            current_row += 1
            break
    else:
        pivot += 1

#RREF
print("Row Reduced Echelon Form of given matrix")
for i in matrix:
    print(i)
#PARAMATERIC
print()
print("Parametric form")
pivots = piv()
free_variables = []
for i in range(columns):
    if i not in pivots:
        free_variables.append(i)
final = []
if columns > rows:
    a = columns-rows
    b = []
    for i in range(columns):
        b.append(0.0)
    for i in range(a):
        matrix.append(b)
rows = len(matrix)
for i in range(len(matrix[0])):
    matrix[i][i] = 1.0
for i in free_variables:
    a = []
    for j in range(rows):
        if i == j:
            a.append(1.0)
        elif matrix[j][i] != 0.0:
            a.append(-matrix[j][i])
        else:
            a.append(0.0)
    final += [str(a)+"x"+str(i+1)]


for i in range(len(final)-1):
    print(final[i],end = "+")
if len(final) != 0:
    print(final[-1])
else:
    print([0]*columns)