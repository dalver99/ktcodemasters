import sys 

N = int(sys.stdin.readline().strip()) 
numlist = list(map(int,sys.stdin.readline().strip().split())) 

for _ in range(20): #귀찮으니까 이렇게 할래요
    numlist.append(-100)
    
expected = []
leftappend = []
for k in range (1,N):
    #expected에는 K가 -2일때부터 N까지 모든 기대치를 다 넣는다!!
    #왜? 주사위의 최소값은 3부터임. 주사위 3나오고 K가 -3이면 점수가 얼만지 문제에 없음. 
     
    #당연히 문제 오류가 또 있음. N이 1이고 숫자가 -100이면, 기대값이 0일때부터 +inf까지 모두 똑같음. 어쩔?20
    
    n = k+3 #K+T의 시작점
    probs = [1,3,6,10,15,21,25,27,27,25,21,15,10,6,3,1]
    # k+T
    
    ev = 0
    for t in range(0,16):
        tempnumlist = numlist.copy()
        for x in range (0,16):
            tempnumlist[x+n-1] += x+3
        ev += probs[t] * tempnumlist[t+n-1]
        
    #sprint(tempnumlist)
    expected.append(ev)
    
print(expected)