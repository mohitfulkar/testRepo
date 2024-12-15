def fun(n):
    fact = 1
    if n == 0 or n == 1:
        return fact
    fact = fact * n
    return fact * fun(n - 1)  # Correctly propagate the result of the recursive call

result = fun(5)
print(result)
