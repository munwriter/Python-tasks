l = input().split()
print(len(list(filter(lambda x: x == x[::-1], l))))