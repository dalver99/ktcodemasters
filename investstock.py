import math

N,K = map(int,input().split())

#아예 성립을 안하는 경우 제외
able = True
if K//100 > N:
    able = False

if (K/100)%2 != N%2:
    able = False

if able:
    r = N/2 + K/2
    print(math.comb(N,r))
else:
    print('0')