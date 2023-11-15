def mergecount(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            count += (mid - i + 1)
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return count

def merge_sort_count(arr, temp, left, right):
    count = 0
    if left < right:
        mid = (left + right) // 2
        count += merge_sort_count(arr, temp, left, mid)
        count += merge_sort_count(arr, temp, mid + 1, right)
        count += mergecount(arr, temp, left, mid, right)
    return count
# Count the inversion
def count_inversions(arr):
    n = len(arr)
    temp = [0] * n
    inversions = merge_sort_count(arr, temp, 0, n - 1)
    return inversions

# Read input
with open("Counting_Inversions_input.txt", "r") as file:
    for line in file:
        # Parse the array  
        array = list(map(int, line.strip().split(',')))
        # Print the array
        print("Array:", ', '.join(map(str, array)))
        # Count inversions and print 
        inv_count = count_inversions(array)
        print("Number of inversions:",inv_count)
        # separate lines
        print()
