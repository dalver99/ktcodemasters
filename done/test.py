import sys
sys.setrecursionlimit(10**6)

N = int(input())
MOD = 1000000007

##행렬 곱셈
def hang_gop(mat1, mat2):
    res = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for z in range(2):
                # 00 01     00 01  *  00 01
                # 10 11  =  10 11  *  10 11
                ## 두개정도만 머릿속으로 해봅시다

                # https://i.imgur.com/TwtqS5e.png

                ##그럼 이제 각 요소는 절대 MOD를 넘을 수 없게 되어버렸음.
                res[i][j] += mat1[i][z] * mat2[z][j] % MOD
    return res

##분할정복 -> 거듭제곱을 나눠서 해보자
def power(a, b):
    if b == 1:  # b의 값이 1이 될 때까지 재귀
        return a
    else:
        tmp = power(a, b // 2)  # a^(b // 2)
        if b % 2 == 0:
            return hang_gop(tmp, tmp)  # b가 짝수인 경우
        else:
            return hang_gop(hang_gop(tmp, tmp), a)  # b가 홀수인 경우


matrix = [[1, 1], [1, 0]]
if N == 0:
    print(0)
else:
    result = power(matrix, N)

    print(result[0][1] % MOD)




_, K = map(int,input().split())
string = input()
result = ''
for each_letter in string:
    result += each_letter*K
print(result)


