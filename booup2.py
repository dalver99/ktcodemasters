import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    able = False
    n,k = map(int,input().split())
    a1,a2 = map(int,input().split())
    b1,b2 = map(int,input().split())

    if a1 > a2: #뭐 이렇게하면 0으로 나누는 일은 없음
        iterate = n//a1
    else:
        iterate = k//a2

    for an in range(iterate+1): #0이 되어도 한번 더해야댐
        if b1 == 0: #한쪽이 0이면, 나눠떨어지는지만 체크
            if n == 0 and k%b2 == 0:
                able = True
                break
        elif b2 == 0:
            if k == 0 and n%b1 == 0:
                able = True
                break
        elif (n%b1 == 0) and (k%b2 == 0): #나눠짐?
            mok = n//b1
            if k == b2*mok:
                able = True
                break

        n -= a1
        k -= a2
        
        if n == 0 and k == 0:
            able = True
            break

        if n < 0 or k < 0:
            break

    if able:
        print('YES')
    else:
        print('NO')