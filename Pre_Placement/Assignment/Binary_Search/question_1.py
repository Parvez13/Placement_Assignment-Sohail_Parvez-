def squareRoot(n):
    low, high = 1, n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return high

x = 20
print(squareRoot(x))
