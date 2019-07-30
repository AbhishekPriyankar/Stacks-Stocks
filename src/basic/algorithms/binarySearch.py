def binary_search(array, lower_index, upper_index, key):
    if upper_index >= 1:
        mid = round(lower_index + ( upper_index - lower_index) / 2)

        if array[mid] == key:
            return mid

        elif array[mid] > key:
            return binary_search(array, lower_index, mid-1, key)

        else :
            return binary_search(array, mid+1, upper_index, key)

    else:
        return -1

arr_length = int(input())

arrayy = []
for i in range(0,arr_length):
    arrayy.append(int(input()))

key = int(input())
result = binary_search(arrayy, 0, len(arrayy) - 1, key)

if result != -1 :
    print( "Element present at ", result+1 )

else:
    print( "Element is not present in Array" )
