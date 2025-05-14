input_str = input("Nhap x, y: ")
demensions = [int(x) for x in input_str.split(',')]
rowN = demensions[0]
colN = demensions[1]
multilist = [[0 for col in range(colN)] for row in range(rowN)]
for row in range(rowN):
    for col in range(colN):
        multilist[row][col] = row * col
print(multilist)