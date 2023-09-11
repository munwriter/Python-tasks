m, n = map(int, input().split())
c = 1
l = [i for i in range(m*n)]
for i in range(m, n*m+1, m):
    print(i, end='')
print(l)

