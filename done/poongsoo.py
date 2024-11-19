N,M = map(int,input().split())

matrix = []
sunwoo = 1

for i in range (N):
    row = []
    row = list(map(str,input()))
    matrix.append(row)

#print(matrix)


#오른쪽 아래로만 탐색
#각행마다 아래로 사각형 찾기
for k in range(N):#맨 아래에선 사각형 못만듬
    for j in range(M):#맨 오른쪽에선 사각형 못만듬
        #이제 각 요소 하나씩을 훑고 있음. 이제 오른쪽으로만 훑자.
        #시작위치는 j+1, 마지막위치는 인덱스상 M-2
        for l in range(j+1,M): #3x3matrix에서 j가 1이면, 1까지만.
            if (matrix[k][j] == matrix[k][l]): #가로에서 먼저 찾아서 아래로 내려가자
                #그 사이는 다 같아?
                if len(set(matrix[k][j:l+1])) ==1:
                    #그럼 아래로 내려가봐
                    height = 1
                    letter = matrix[k][j]
                    for m in range (k+1,N): #현재Y좌표부터 아래로 하나씩
                        if len(set(matrix[m][j:l+1])) == 1 and matrix[m][j] == letter: #다음행도 기존것과 다 똑같니?
                            height += 1
                            #print(f"HEIGHT ADDED from row {k}{j} to {k}{l} with height {height}")
                    sunwoo = max(sunwoo,(l-j+1)*height)
                
                
                    # if (matrix[k][j] == matrix[k+l-j][j]) and (matrix[k][j] == matrix[k+l-j][l]):
                    #     print(f"FOUND! [{k},{j}], length = {l-j}")
                    #     sunwoo = max((l-j)**2,sunwoo)
                
print(sunwoo)  