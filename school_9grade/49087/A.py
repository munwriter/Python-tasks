n = int(input())
l = [input() for i in range(n)]
print(*list(filter(lambda x: x[0] != x[-1], l)))