# Bubble sort

data = [2, 5, 7, 1, 3, 8, 4, 100, 6, 140]


def bubble_sort(array):
    for i in range(len(array)-1):
        j = i+1
        while j <= (len(array)-1):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
            j += 1

    return array


print(bubble_sort(data))
