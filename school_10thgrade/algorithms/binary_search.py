def binary_search(value, array):
    top = len(array) - 1
    bot = 0
    while bot <= top:
        middle_index = (top + bot) // 2
        middle_value = array[middle_index]
        if middle_value < value:
            bot = middle_index + 1
        elif middle_value > value:
            top = middle_index - 1
        else:
            return middle_index