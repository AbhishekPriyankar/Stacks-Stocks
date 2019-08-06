# The idea of formula is to return higher value of pos
# when element to be searched is closer to arr[hi]. And
# smaller value when closer to arr[lo]
# pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

# arr[] ==> Array where elements need to be searched
# x     ==> Element to be searched
# lo    ==> Starting index in arr[]
# hi    ==> Ending index in arr[]

def interpolationSearch(arr, n ,x):
    low = 0
    high = (n-1)

    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low;
            return -1;

        # Probing the position with keeping
        # uniform distribution in mind.
        pos = low + int((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            low = pos + 1

        else:
            high = pos - 1

    return -1

arr_length = int(input())

arrayy = []
for i in range(0,arr_length):
    arrayy.append(int(input()))

key = int(input())

index = interpolationSearch(arrayy, arr_length, key)

if index != -1:
    print("Element found at index ", index+1)
else:
    print("Element not found")
