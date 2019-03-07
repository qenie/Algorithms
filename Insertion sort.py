# Insertion sort

data = [2, 5, 7, 1]


def insertion_sort(array):
    for index in range(1, len(array)):
        current = array[index]
        position = index

        while position > 0 and array[position-1] > current:
            array[position] = array[position-1]
            position -= 1

        array[position] = current

    return array


print(insertion_sort(data))
