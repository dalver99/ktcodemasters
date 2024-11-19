from fractions import Fraction
#분수로 계산하자 제발.
import sys

N,K,A,B,C,X = map(int,sys.stdin.readline().split())

#트리구조의 연산이다. 1분마다 각 층에 대해 순서와 관계없이 수행해서 새로운 행렬을 만들어 주기만 하면 됨. 과거와 현재를 가지고만 있으면 됨
#고작해야 8층임. 그냥 다 돌리는 게 맞을듯

#나가는 건 0일때, 1,2,3,4 4층기준이면 5는 위로 나간거. 그니까.. N보다 2 큰 행렬이 필요
past = [Fraction(0,1) for _ in range (N+2)]
future = [Fraction(0,1) for _ in range (N+2)]
#여기서부터 시작 (0분)
past[K] =  Fraction(1,1)


#X번 반복
for i in range (X): #N분동안 반복
    future[0] += past[0]
    future[N+1] += past[N+1]
    
    for j in range (1,N+1): #0은 안셈, 1,2,3..N층까지 가야함!
        #각 층에서 세갈래로 뻗어나가자
        if past[j] != 0: #0이면 넘어가도 됨.
            #아래층으로 내려가기
            future[j-1] += (past[j] * Fraction(B,A+B+C))
            #올라가기
            future[j+1] += (past[j] * Fraction(A,A+B+C))
            #가만히 있기
            future[j] += (past[j] * Fraction(C,A+B+C))

    #자 근데 0층과 꼭대기층은 다시 더해줘야함.
    past = future #의미심장한 문장이다. 과거라는 건 항상 어떤 시점의 미래가 대입된 것이 아닌가?
    future = [Fraction(0,1) for _ in range (N+2)]

escape = past[0] + past[N+1]


print(" ".join("{}/{}".format(past[k].numerator, past[k].denominator) for k in range(1, N+1)))
print("{}/{}".format(escape.numerator, escape.denominator))