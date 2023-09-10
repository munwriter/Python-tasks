l=[]
for i in range(int(input())):
    l+=input().split(',')
print(l[l.index(input())+1])