def insertion_sort(array):
    for i in range(1, len(array)):
        previous_element_index = i - 1
        while array[previous_element_index] > array[i] and previous_element_index >= 0:
            array[previous_element_index], array[i] = array[i], array[previous_element_index]
            previous_element_index -= 1
            i -= 1
    return array
