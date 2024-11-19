R=5**(0.5)
MOD = 1000000007
N = int(input())
def fibo_ilbanhang(n):
    result = 1
    while n > 1000:
        result *= round(((1+R)/2)**1000/R)
        n -= 1000
    if n <= 1000:
        result *= round(((1+R)/2)**n/R)
    return result

print(int(fibo_ilbanhang(N+1))%MOD)



# import sys
# def fibo_ilbanhang(n):
#     r=5**(0.5)
#     return round(((1+r)/2)**n/r)

# input = sys.stdin.readline
# N = int(input())
# sys.stdout.write(str(int(fibo_ilbanhang(N+1))%1000000007))


N = int(input())
N+= 1
MOD = 1000000007
hang_count = 0
power_count = 0

##행렬 곱셈
def hang_gop(mat1, mat2):
    global hang_count
    hang_count += 1
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                # 00 01     00 01     00 01
                # 10 11  =  10 11  *  10 11
                ##그럼 이제 각 요소는 절대 MOD를 넘을 수 없게 되어버렸음.
                res[i][j] += mat1[i][z] * mat2[z][j] % MOD
    return res

##분할정복 -> 거듭제곱을 나눠서 해보자
def power(a, b):
    global power_count
    power_count += 1
    if b == 1:  ##b의 값이 1이 될 때까지 재귀
        return a
    else:
        tmp = power(a, b // 2)  ## b = b // 2 ( + 1 )
        if b % 2 == 0:
            return hang_gop(tmp, tmp)  ## b가 짝수인 경우
        else:
            return hang_gop(hang_gop(tmp, tmp), a)  ## b가 홀수인 경우


matrix = [[1, 1], [1, 0]]
result = power(matrix, N)

print(result[0][1] % 1000000007)
print("power_count: ",power_count)



#print("hang_count: ",hang_count)