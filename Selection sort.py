# Selection sort

data = [2, 5, 7, 1, 3, 8, 4, 100, 6, 140]


def selection_sort(array):
    for i in range(len(array)-1):
        index = i
        j = i+1
        while j <= (len(array)-1):
            if array[j] < array[index]:
                index = j
            j += 1
        array[i], array[index] = array[index], array[i]

    return array


print(selection_sort(data))
