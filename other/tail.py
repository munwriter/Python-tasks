# A fairy tale about the most terrible ghost that no one has ever seen 
# The tale of the black black black night 
# The tale of the incredible book of the most terrible spells 
# A fairy tale about the transformations of the sweetest into the most terrible
parity = 1
l = input().split()
# s = [i.split() for i in l]
origin_l = l[::]


for i in range(len(l)):
    if l[i][0].isupper():
        if i%2!= 0:
            parity = 0
        else:
            parity = 1
        continue
    else:
        if parity == 1:
            if i%2 == 0:
                origin_l[i] = ''
        if parity == 0:
            if i%2!= 0:
                origin_l[i] = ''
print(origin_l)


