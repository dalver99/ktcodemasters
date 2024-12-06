import sys
from itertools import product

m, n = map(int, sys.stdin.readline().strip().split())

def colorTheGrid(m, n):
    colors = [0, 1, 2]
    
    #첫 행에서 가능한 것을 모두 나열
    valid_patterns = []

    ##모든 경우의수를 다 놓고, 안되는 걸 일단 한 row에서 제외함
    row_possible = 0
    for pattern in product(colors, repeat=m):
        if all(pattern[i] != pattern[i+1] for i in range(m-1)):
            row_possible += 1
            valid_patterns.append(pattern)
    #print(row_possible)
    
    #각 row 밑에 올 수 있는 패턴들을 확인해봄
    adjacent_patterns = {}
    adj_possible = 0
    for pattern in valid_patterns:
        adjacent_patterns[pattern] = []
        for next_pattern in valid_patterns:
            if all(item1 != item2 for item1, item2 in zip(pattern, next_pattern)):
                adj_possible += 1
                adjacent_patterns[pattern].append(next_pattern)

    # for key,value in adjacent_patterns.items():
    #     print(len(value))
    #1. 점화식으로 풀기

    #2. DP로 풀기
    dp = {}
    for pattern in valid_patterns:
        dp[pattern] = 1
    
    #남은 행들에 대해 수행
    new_dp = {}
    for pattern in valid_patterns:
        new_dp[pattern] = 0
    for _ in range(n - 1):
        temp_dp = {}
        for pattern in valid_patterns:
            temp_dp[pattern] = 0
            for prev_pattern in adjacent_patterns[pattern]:
                temp_dp[pattern] += dp[prev_pattern]
        dp = temp_dp.copy()
    
    return dp

dp = colorTheGrid(m, n)
print(dp)
print(sum(dp.values()))

