import math

def binary_search(arr, num_search):
    found = False
    left_idx = 0
    right_idx = len(arr) - 1
    for i in range(len(arr)):
        pointer_idx = math.floor((left_idx + right_idx) / 2)
        if num_search == arr[pointer_idx]:
            found = True
            break
        elif num_search > arr[pointer_idx]:
            left_idx = pointer_idx + 1
        else:
            right_idx = pointer_idx - 1
    return found

arr = [0, 5, 7, 9, 15, 16]
print(binary_search(arr, 30))