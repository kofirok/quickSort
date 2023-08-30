def partition(array, low, high, comparisons, assignments):
    # Select the pivot element as the last element in the sub array
    pivot = array[high]

    # Initialize the index of the pivot element
    i = low - 1

    # Loop through the elements in the sub array
    for j in range(low, high):
        # Increment the number of comparisons
        comparisons += 1

        # If the current element is less than or equal to the pivot,
        # swap it with the element at index i + 1
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            # Increment the number of assignments
            assignments += 1

    # Swap the pivot element with the element at index i + 1
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Increment the number of assignments
    assignments += 1

    # Return the index of the pivot element and the updated values for comparisons and assignments
    return i + 1, comparisons, assignments

def quickSort(array, low, high, comparisons, assignments):
    # If the low index is less than the high index,
    # That means there are still elements in the sub array to sort
    if low < high:
        # Partition the sub array and gather the number of comparisons and assignments
        part, c, a = partition(array, low, high, comparisons, assignments)

        # Increment the number of comparisons and assignments
        comparisons += c
        assignments += a

        # Recursively sort the sub arrays to the left and right of the pivot element
        quickSort(array, low, part - 1, comparisons, assignments)
        quickSort(array, part + 1, high, comparisons, assignments)

    # Return the sorted array and the number of comparisons and assignments
    return array, comparisons, assignments
