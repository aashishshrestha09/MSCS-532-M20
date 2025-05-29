def quick_sort(arr):
    """Sorts the array using the Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr  # Base case: a single-element list is already sorted

    # Choose the pivot (middle element for better average performance)
    pivot = arr[len(arr) // 2]

    # Partition the array into three lists: less than, equal to, and greater than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)
