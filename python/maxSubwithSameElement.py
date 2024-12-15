def count_ele(arr):
    n = len(arr)
    count = 1
    maxi = float('-inf')
    for i in range(n-1):
        if(arr[i]==arr[i+1]):
            count+=1
        else:
            count=1
        maxi = max(count,maxi)
    return maxi

arr = [2,2,3,3,3,3,-3,-3,-3,-3,-3,-2,-1,4]
result = count_ele(arr)
print(f"Result is {result}")

