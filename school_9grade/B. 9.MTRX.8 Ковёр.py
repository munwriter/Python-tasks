n = int(input())
l = [[0]*8 for i in range(8)]

for i in range(n):
    row, col = map(int,input().split())
    l[row-1][col-1] = 1

max = 0
res = []
for i in range(7):
    for j in range(7):
        if l[i][j] + l[i][j+1] + l[i+1][j] + l[i+1][j+1] > max:
            max = l[i][j] + l[i][j+1] + l[i+1][j] + l[i+1][j+1]
            res = [i+1,j+1]

print(*res)