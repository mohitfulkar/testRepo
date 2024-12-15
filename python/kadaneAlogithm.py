def kadaneAlgo(arr):
    n = len(arr)
    current_sum = 0  
    max_sum = float('-inf') 

    for i in range(n):
        current_sum += arr[i] 
        max_sum = max(max_sum, current_sum)  
        if current_sum < 0:  
            current_sum = 0

    print(max_sum)

# Example usage
arr = [-4,-6,-3,-6]
kadaneAlgo(arr)
