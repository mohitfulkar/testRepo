def longest_subarray_with_least_difference(arr):
    n = len(arr)
    if n == 1:
        return arr
    
    max_diff = float('inf')
    longest_length = 0
    best_start = 0  # To track the start index of the subarray with the least difference
    best_end = 0  # To track the end index of the subarray with the least difference

    for start in range(n):
        min_val = arr[start]
        max_val = arr[start]
        
        for end in range(start, n):
            # Update the min and max for the current subarray
            min_val = min(min_val, arr[end])
            max_val = max(max_val, arr[end])
            diff = max_val - min_val

            # Check if we have found a new minimum difference or a longer subarray with the same difference
            if diff < max_diff:
                max_diff = diff
                longest_length = end - start + 1
                best_start = start
                best_end = end
            elif diff == max_diff:
                if end - start + 1 > longest_length:
                    longest_length = end - start + 1
                    best_start = start
                    best_end = end
    
    # Return the longest subarray with the least difference
    return arr[best_start:best_end + 1]

# Example usage
arr = [1, 2, 3, 5, 7, 9, 11, 12, 13, 14, 15]
longest_subarray = longest_subarray_with_least_difference(arr)
print("Longest subarray with the least difference:", longest_subarray)
