import sys
import math
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    able = False
    n,k = map(int,input().split())
    a1,a2 = map(int,input().split())
    b1,b2 = map(int,input().split())

    D = a1*b2 - a2*b1

    if D == 0:
        if a1 == 0 and b1 == 0:
            if n == 0:
                #g2 = math.gcd(a2,b2)
                #if k%g2 == 0: #정수해가 존재는 하는 상황
                iter = k // a2
                for _ in range(iter+2):
                    if k%b2 == 0:
                        able = True
                        break
                    k -= a2
                    if k == 0:
                        able = True
                        break
                    if k < 0:
                        break
        elif a2 == 0 and b2 == 0:
            if k == 0:
                #g1 = math.gcd(a1,b1)
                #if n%g1 == 0: #정수해가 존재는 하는 상황
                iter = n // a1
                for _ in range(iter+2):
                    if n%b1 == 0:
                        able = True
                        break
                    n -= a1
                    if n == 0:
                        able = True
                        break
                    if n < 0:
                        break                        
        elif a1/a2 == n/k:
            #g1 = math.gcd(a1,b1)
            #if n%g1 == 0: #정수해가 존재는 하는 상황
            iter = n // a1
            for _ in range(iter+2):
                if n%b1 == 0:
                    able = True
                    break
                n -= a1
                if n == 0:
                    able = True
                    break
                if n < 0:
                    break                       
    else: #D!=0, 솔루션은 반드시 존재, 두 직선의 교차점 좌표가 모두 음이아닌 정수인지만 체크하면 됨
        x_num = b2*n - b1*k
        y_num = a1*k - a2*n
        x,x_rem = divmod(x_num,D)
        y,y_rem = divmod(y_num,D)
        #print(x,y)
        if x_rem == 0 and y_rem == 0 and x >= 0 and y >= 0:
            able = True

    if able:
        print('YES')
    else:
        print('NO')