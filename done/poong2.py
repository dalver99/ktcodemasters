N,M = map(int,input().split())

matrix = []
sunwoo = 1

for i in range (N):
    row = []
    row = list(map(str,input()))
    matrix.append(row)

for k in range(N):
    for j in range(M):
        for l in range(j+1,M): 
            if (matrix[k][j] == matrix[k][l]): 
                if len(set(matrix[k][j:l+1])) ==1:
                    height = 1
                    letter = matrix[k][j]
                    for m in range (k+1,N): 
                        if len(set(matrix[m][j:l+1])) == 1 and matrix[m][j] == letter:
                            height += 1
                    sunwoo = max(sunwoo,(l-j+1)*height)  
    
                
print(sunwoo)  