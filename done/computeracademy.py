def place_students(N):
    dp = [0] * (N + 2)
    dp[1] = 3
    dp[2] = 7

    for i in range(3, N+1):
        dp[i] = (dp[i-1] * 2 + dp[i-2])
    return dp[N] % 796796

# Input
N = int(input())
output = place_students(N)
print(output)