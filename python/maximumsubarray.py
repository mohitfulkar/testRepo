def maximum_subarray(nums):
    n = len(nums)
    max_sum = float('-inf')  # Initialize to the smallest possible value

    for i in range(n):
        current_sum = 0  # Reset the sum for each new starting index
        for j in range(i, n):  # Compute the sum of subarray starting from 'i'
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)  # Update the max sum if current sum is greater

    return max_sum


# Example usage
nums = [2, 3, 4, -9, -34, 5, 6, -3]
result = maximum_subarray(nums)
print("Maximum Subarray Sum:", result)
