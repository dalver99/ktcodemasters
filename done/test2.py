MOD = 1000000007

def matrix_mult(A, B, mod=MOD):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod]]

def matrix_pow(matrix, n, mod=MOD):
    result = [[1, 0], [0, 1]]
    base = matrix
    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base, mod)
        base = matrix_mult(base, base, mod)
        n //= 2
    return result

def mold_count(N):
    # 초기 상태: [번식 가능한 곰팡이 수, 포자 수] = [1, 1]
    if N == 0:
        return 1  # 초기 포자 1개
    # 변환 행렬
    transition_matrix = [[1, 1], [1, 0]]
    # N분 후의 행렬
    result_matrix = matrix_pow(transition_matrix, N, MOD)
    # 총 곰팡이 수: 번식 가능한 곰팡이 수 + 포자 수
    return (result_matrix[0][0] + result_matrix[0][1]) % MOD

# 입력
N = int(input())
N -= 1
print(mold_count(N))
