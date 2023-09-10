def zamena_top(l):
    zero_counter = 0
    for elem in range(n):
        if l[elem] == 0:
            zero_counter += 1
        elif  zero_counter == 0:
            l[elem] = 4
        elif zero_counter == 1:
            l[elem] = 1
        else:
            l[elem] = 2
    return l

def zamena_bottom(l):
    zero_counter = 0
    for elem in range(n):
        if l[elem] == 0:
            zero_counter += 1
        elif  zero_counter == 0:
            l[elem] = 4
        elif zero_counter == 1:
            l[elem] = 3
        else:
            l[elem] = 2
    return l

n = int(input())
l = [1]*n
l[0], l[-1] = 0, 0
j = 1
print(*[0]+[1]*(n-2)+[0])
for i in range(n-2):
    l  = [1]*n
    l[j] = 0
    l[-j-1] = 0
    j += 1
    if i<n//2:
        l = zamena_top(l)
    else:
        l = zamena_bottom(l)

    if n%2!=0:
        if i+1 == ((n-2)//2+1):
            print(*([4]*(n//2))+[0]+([2]*(n//2)))
        else:
            print(*l)
    else:
        print(*l)

print(*[0]+[3]*(n-2)+[0])
