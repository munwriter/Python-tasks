def p(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

l = input().split()

dop_it = 0

for i in range(len(l)):
    if p(int(l[i + dop_it])):
        l.insert(i + 1 + dop_it, sum(map(int, (str(l[i + dop_it])))))
        dop_it += 1

print(l)
