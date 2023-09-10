s=input()
ss=''

for i in range(len(s)):
    if i%2==0:
        if 'a'<=s[i]<='z':
            ss+=chr(ord('A')+(ord(s[i])-ord('a')))
        else:
            ss+=s[i]
    else:
        if 'A'<=s[i]<='Z':
            ss+=chr(ord('a')+(ord(s[i])-ord('A')))
        else:
            ss+=s[i]

print(ss)