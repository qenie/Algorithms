# Binary search

data = [2, 3, 4, 5, 7, 8, 10, 14, 18, 100, 140]


def binary_search(collection, number):

    if number not in data:
        return 0
    if number > (collection[len(collection) - 1]):
        return -1

    elif number < collection[0]:
        return -2

    else:
        left = 0                                  # Left index of collection
        right = len(collection) - 1               # Right index of collection
        while left <= right:
            mid = (left + right) // 2             # Medium index
            current_item = collection[mid]        # Medium item in the collection
            if current_item == number:
                return mid + 1
            elif current_item > number:
                right = mid - 1
            elif current_item < number:
                left = mid + 1


print("The sorted collection is", data)
index = binary_search(data, int(input("Enter a number to search:")))
if index == -1:
    print("Entered number bigger than data in array")
elif index == -2:
    print("Entered number less than data in array")
elif index == 0:
    print("There is no such number in the collection")
else:
    print("The position of entered number is:", index)
