s = list(input().split('+'))
sum = 0

for i in range(len(s)-1):
    if s[i][-1].isdigit() and s[i+1][0].isdigit():
        sum += int(s[i][-1]) + int(s[i+1][0])
        s[i+1] = '0' + s[i+1][1:]
print(sum)