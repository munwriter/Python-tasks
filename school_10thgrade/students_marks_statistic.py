def foo(names: list[str],  marks: list[list[int]]):
    global longest_name
    longest_name = len(max(names))
    res = []
    for i in range(len(names)):
        res_data = [names[i], middle(marks[i]), median(sorted(marks[i]))]
        res.append(res_data)
    return sorted(res)


def middle(l):
    return sum(l)/len(l)


def median(l):
    if len(l) % 2 == 0:
        return (l[len(l)//2] + l[len(l)//2-1])/2
    else:
        return l[len(l)//2]


r = foo(['b', 'abb', 'cccf'],
               [[3, 4, 5, 2],
                [4, 5, 5, 5],
                [3, 3, 3]])

for i in range(len(r)):
    print(
        f'Name:{r[i][0]:>{longest_name + 2}}, middle:{r[i][1]:>5.1f}, median:{r[i][2]:>5.1f}')
