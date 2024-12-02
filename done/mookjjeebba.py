import math

N,M = map(int,input().split())
n_list = list(map(int,input().split()))
m_list = list(map(int,input().split()))

# IDEA 1 - 최소공배수번까지 진행되면 반복된다!
lcm = math.lcm(N,M)

# N이 2고 M이 3이면 이렇게 된다
# 0 0 // 1 1 // 0 2 // 1 0 // 0 1 // 1 2 
# i는 0,1,2,3,4,5

# 이건 좀 사람이 해석하기 어려우니까
# 1 1 // 2 2 // 1 3 // 2 1 // 1 2 // 2 3 >> 이거말고
# 0 0 // 1 1 // 0 2 // 1 0 // 0 1 // 1 2 
# i는 1 2 3 4 5 6 진행된다고 하면
# i mod2 i mod 3 // ... 로 진행된다!
who_won = 0
sungong = 0 #1이면N, 2면M이 선공인 상태라고 하자

for i in range (lcm):
    # IDEA 2 - 나눈 나머지로 빙빙 돌리면 된다!
    n_played = n_list[i%N]
    m_played = m_list[i%M]
    #print(n_played,m_played)

    if sungong == 0: #아직 시작하고나서 선공이 정해진 적이 없음. 여기서 무승부가 나도 이 상태로 유지되어야 하며, 이게 문제에 주어져있지 않은 것은 미스라고 생각함.
        if (n_played - m_played)%3 == 1: #N이 이김. 영어로는 가위바위보가 이 순서가 아니라 챗지피티야 요건 몰랐지?
            sungong = 1
        elif (m_played - n_played)%3 == 1:
            sungong = 2
    elif sungong == 1: #N이 이기고 있는 경우
        if n_played == m_played: #결판이 났따
            who_won = 1
            break
        elif (n_played - m_played)%3 == 1: #지속되는 경우들
            sungong = 1
        elif (m_played - n_played)%3 == 1:
            sungong = 2
    elif sungong == 2: #N이 이기고 있는 경우
        if n_played == m_played: #결판이 났따
            who_won = 2
            break
        elif (n_played - m_played)%3 == 1: #지속되는 경우들
            sungong = 1
        elif (m_played - n_played)%3 == 1:
            sungong = 2

print(who_won)