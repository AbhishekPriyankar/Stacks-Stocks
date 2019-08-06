import math

def jump_search(array, key, arr_len):

    step = math.sqrt(arr_len)
    previous = 0

    # Finding the block where element is
    # present (if it is present)
    while array[int(min(step, arr_len)-1)] < key:
        previous = step
        step += math.sqrt(arr_len)

        if previous >= arr_len:
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while array[int(previous)] < key:
        previous += 1

        # If we reached next block or end
        # of array, element is not present.
        if previous == min(step, arr_len):
            return  -1

    # If the element is found
    if array[int(previous)] == key:
        return previous

    return -1

arr_len = int(input())
array = []

for i in range(0, arr_len):
    array.append(int(input()))

key = int(input())

index = jump_search(array, key, arr_len)

print("Number ", key, "at index ", "%.0f"%index)
