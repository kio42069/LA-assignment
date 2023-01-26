mtx = []
with open(r"C:\Users\Dell\Desktop\Coding\linalg.txt","r") as file:
    rows = int(file.readline())
    columns = int(file.readline())
    while True:
        record = file.readline()
        if record != "":
            record = list(map(float,record.split()))
            mtx.append(record)
        else:
            break


def ToReducedRowEchelonForm(M):
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i], M[r] = M[r], M[i]
        lv = M[r][lead]
        M[r] = [mrx / lv for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [(iv - lv * rv) for rv, iv in zip(M[r], M[i])]
        lead += 1

ToReducedRowEchelonForm(mtx)
for i in mtx:
    print(i)
"""for rw in mtx:
    print(', '.join(str(x) for x in rw))"""
