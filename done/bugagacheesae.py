import math

A = int(input().strip())
divided = A/11
if str(divided).split('.')[1][0] == '9':
    print(-1)
else:
    buga = math.floor(divided)
    price = A-buga
    print(f'{price} {buga}')

#21같은건 안됨. 왜? 21/11 = 1.909. 19로해도 안되고, 20으로해도 안됨.
#98도 안됨. 왜?? 98/11 = 8.909 89로해도 안되고, 90으로 해도 안됨. 

#공통점은, 11로 나눴을 때 9로 끝난다는 점임. 97/11은 8.8이지만, 89로하면 할 수 있음!!

#1을 더하거나 (뺐을때) 자리수가 바뀌어버리면 곤란한 경우구나.
#그럼 11로 나눴을때 1로 끝나면? > 딱히 문제 없음
#0으로 끝나면? > 문제 없음
#자리수가 올라가는 문제로, 내려가는 방향은 전혀 문제 없으며 자리수 변동이 없는 경우 또한 문제 없음!


##EQUIVALENT OF

#A = int(input().strip())
#print(-1 if str(A/11).split('.')[1][0] == '9' else f'{A - A//11} {A//11}')