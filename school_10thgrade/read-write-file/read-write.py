def get(path):
    with open(path, 'tr', encoding='utf-8') as input:
        read_result = []
        for line in input.readlines():
            row = line.rstrip().split(',')
            read_result.append(row)
    return read_result


def format_data(data):
    data = sorted(data)
    data = [f'Country: {i[0]}, Capital: {i[1]}\n' for i in data]
    return data


def post(path, data):
    with open(path, 'tw') as output:
        output.writelines(data)


input_path = 'C:\\Users\\vysok\\Desktop\\Python tasks\\school_10thgrade\\read-write-file\\input.txt'
output_path = 'C:\\Users\\vysok\\Desktop\\Python tasks\\school_10thgrade\\read-write-file\\output.txt'
post(output_path, format_data(get(input_path)))


