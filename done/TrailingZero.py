def trailing_zero_count(x):
    count = 0
    while x >= 5:
        x //= 5
        count += x
    return count

def find_minimum_trailing_zero(n):
    left, right = 0, n * 5  # upper bound is sufficient to find the answer
    result = -1

    while left <= right:
        mid = (left + right) // 2
        zeros = trailing_zero_count(mid)

        if zeros >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

n = int(input())
result = find_minimum_trailing_zero(n)
print(result)