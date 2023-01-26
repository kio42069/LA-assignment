#Row Reduction Algorithm


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
rowC = rows      #keeping a copy of initial rows since we are removing it nowk

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
for i in range(rows):
    pivots = piv()
    for t in range(i+1,rows):
        pivots = piv()
        if pivots[i] == pivots[t]:
            makeone()
            gol(3)
            subtract(i,t)

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

temp = matrix.copy()
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
    

print("Row Reduced Echelon Form of given matrix")
for i in matrix:
    print(i)

#Paramentric form
matrix = temp.copy()
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if str(matrix[i][j]) == '-0.0':
            matrix[i][j] = 0.0

print()
#taking transpose of the RREF matrix
transpose = []
for j in range(columns):
    newRow = [matrix[i][j] for i in range(rows)]
    transpose.append(newRow)
for i in transpose:
    print(i)
    
if rows > columns :
    print("No solution for the given matrix")
else:
    if rows != columns:
        if sorted(pivots) != pivots:
            new = []
            for i in range(len(pivots)):
                new = new + [[]]
            for i in range(len(pivots)):
                new[pivots.index(min(pivots))] = matrix[i]
            matrix = new
        a = columns-rows
        b = []
        for i in range(columns):
            b = b + [0.0]
        for i in range(a):
            matrix = matrix + [b]
            
            
print()
print()
for i in range(len(matrix)):
    print(matrix[i])