def solution(grid, t):
    N = len(grid)
    list_k = []
    
    #약수부터 체크
    for i in range(2, int(N/2)+1):
        if N%i == 0:
            list_k.append(i)

    #N을 2차리스트로 제정리
    grid2 = []
    for each_row in grid:
        listed_row = list(each_row)
        grid2.append(listed_row)

    #N이 소수면 답이 없음.
    if len(list_k) == 0:
        return 0

    max_k = 0
    # 이제 하나씩 시도해보자... 해당 박스를 각각 set에 넣고 길이를 재면 됨
    # 박스의 개수는 (N/k)**2, N=6,k=2면 각 박스의 인덱스는 0,2,4. 0,0~1,1
    for candi_k in list_k: #candi_k = 2
        candi_ts = []
        for y in range(int(N/candi_k)): #0,1,2
            for x in range(int(N/candi_k)): #0,1,2 #행을 넣고, 그안에
                # x:0 > 0-1 #x:1 > 2-3 #x:2 > 4~5
                elements = []
                for yy in range(y*candi_k, (y+1)*candi_k):
                    for xx in range(x*candi_k, (x+1)*candi_k):
                        elements.append(grid2[xx][yy])

                setted = set(elements)
                candi_ts.append(len(setted))
        if max(candi_ts) <= t:
            max_k = max(max_k, candi_k)

    answer = max_k
    return answer