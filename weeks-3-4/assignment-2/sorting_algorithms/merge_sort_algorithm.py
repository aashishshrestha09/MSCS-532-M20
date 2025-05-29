def merge(left, right):
    """Merges two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    """Recursively divides the array and merges sorted halves."""
    if len(arr) <= 1:
        return arr  # Base case: a single-element list is already sorted

    # Find the middle point
    mid = len(arr) // 2

    # Recursively sort left and right halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left, right)
