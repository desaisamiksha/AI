def selection_sort_descending(arr):
    
    for i in range(len(arr)):
        
        max_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


array = [64, 25, 12, 22, 11]
sorted_array = selection_sort_descending(array)
print("Sorted array in descending order:", sorted_array)