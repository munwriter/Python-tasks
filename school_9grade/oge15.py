n = int(input())
l = [int(input()) for i in range(n)]
print(max(filter(lambda x: x % 5 == 0, l)))