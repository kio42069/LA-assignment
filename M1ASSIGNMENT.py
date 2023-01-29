#Row Reduction Algorithm

print()
matrix = []
#returns pivot positions
def piv():
    global matrix
    pivots = []
    for i in matrix:
        for j in i:
            if j != 0:
                pivots.append(i.index(j))
                break 
    return pivots   


#rounds off the matrix
def gol(n):
    new = []
    global matrix
    for i in matrix:
        a = []
        for j in i:
            a.append(round(j,n))
        new.append(a)
    matrix = new.copy()

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
rowC = rows      #keeping a copy of initial rows since we are removing it now

#removing lines of format 0 0 0 0 etc. with no non zero values
i = 0
while i < rows:
    flag = 1
    for j in range(columns):
        if matrix[i][j] != 0:
            flag = 0
            break
    if flag == 1:
        matrix.remove(matrix[i])
        rows -= 1
    else:
        i += 1



#sorting the matrix (partial echelon form)
done = []
i = 0
j = 0
while j < columns:
    limit = 0
    while i < rows:
        if limit == rows:
            break
        elif matrix[i][j] == 0:
            removeit = matrix.pop(i)
            matrix.append(removeit)
        else:
            i += 1
        limit += 1
    for k in range(i,rows):
        if [matrix[x][j] for x in range(rows)][k] == 0:
            i = k
            break
    j += 1



#making pivot positions 1
def makeone():
    pivots = piv()
    for i in range(rows):
        try:
            pivot = matrix[i][pivots[i]]
            for j in range(columns):
                matrix[i][j] = matrix[i][j]/pivot
        except:
            continue


#subtract row with index a from row with index b
def subtract(a,b):
    for _ in range(len(matrix[a])):
        matrix[b][_] = matrix[b][_] - matrix[a][_]





#echelon form
i = 0
while i < rows:
    pivots = piv()
    t = i+1
    while t < rows:
        pivots = piv()
        if pivots[i] == pivots[t]:
            makeone()
            subtract(i,t)
            makeone()
            gol(3)
            #removing lines of format 0 0 0 0 etc. with no non zero values
            q = 0
            while q < rows:
                flag = 1
                for w in range(columns):
                    if matrix[q][w] != 0:
                        flag = 0
                        break
                if flag == 1:
                    matrix.remove(matrix[q])
                    rows -= 1
                q += 1
        t += 1
    i += 1

#sorting the matrix again in case something got messed up
done = []
i = 0
j = 0
while j < columns:
    limit = 0
    while i < rows:
        if limit == rows:
            break
        elif matrix[i][j] == 0:
            removeit = matrix.pop(i)
            matrix.append(removeit)
        else:
            i += 1
        limit += 1
    for k in range(i,rows):
        if [matrix[x][j] for x in range(rows)][k] == 0:
            i = k
            break
    j += 1
gol(5)
makeone()
gol(5)



#removing lines of format 0 0 0 0 etc. with no non zero values
i = 0
while i < rows:
    flag = 1
    for j in range(columns):
        if matrix[i][j] != 0:
            flag = 0
            break
    if flag == 1:
        matrix.remove(matrix[i])
        rows -= 1
    i += 1


#row reduction
pivots = piv()
for i in range(1,rows):
    for q in range(1,i+1):
        multiplicator = matrix[i-q][pivots[i]]
        newrow = []
        newRow = [x*multiplicator for x in matrix[i]]
        for j in range(pivots[i],columns):
            matrix[i-q][j] = matrix[i-q][j]-newRow[j]
gol(3)

#adding the 0 0 0 0 etc. rows wih no non zero elements back to the matrix
if sorted(pivots) != pivots:
    new = []
    for i in range(len(pivots)):
        new = new + [[]]
    for i in range(len(pivots)):
        new[pivots.index(min(pivots))] = matrix[i]
    matrix = new
a = rowC-rows
b = []
for i in range(columns):
    b = b + [0.0]
for i in range(a):
    matrix = matrix + [b]



#sorting the matrix (partial echelon form)
done = []
i = 0
j = 0
while j < columns:
    limit = 0
    while i < rows:
        if limit == rows:
            break
        elif matrix[i][j] == 0:
            removeit = matrix.pop(i)
            matrix.append(removeit)
        else:
            i += 1
        limit += 1
    for k in range(i,rows):
        if [matrix[x][j] for x in range(rows)][k] == 0:
            i = k
            break
    j += 1


#converting all -0.0's to 0.0's
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if str(matrix[i][j]) == '-0.0':
            matrix[i][j] = 0.0

print("Row Reduced Echelon Form of given matrix")
for i in matrix:
    print(i)

#Parametric Form of the equation
rows = rowC
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