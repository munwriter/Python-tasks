s,ss=input().split()
l,c1,c2=map(int, input().split())
r=""
while len(r)<=l:
    r+=s*c1+ss*c2
print(r[:l])