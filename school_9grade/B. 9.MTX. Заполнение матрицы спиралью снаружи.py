mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]

sum = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        if len(mat) % 2 == 0:
            if j == i:
                sum += mat[i][j]
            elif i + j == len(mat[i]) + 1:
                sum += mat[i][j]
        else:
            if j == i:
                sum += mat[i][j]
            elif i + j == len(mat[i]) - 1:
                sum += mat[i][j]

print(sum)