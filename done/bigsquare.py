N,M = map(int,input().split())
max_area = 0
classs=[]
for _ in range (N):
    row = list(map(int,input().strip().split()))
    classs.append(row)

#사각형이 되려면 그 행 안에 숫자가 반드시 같은 게 있어야 함 (두개 이상일 수 있음), 리스트에 하나를 넣고, 두번째게 들어오면 확인, 없으면 첫번째 걸 드롭, 있으면 최대값에 갱신 > 파기

#list of lists 활용

# for i,row in enumerate(classs): #각 행에서
#     candidates = []
#     for j,num in enumerate(row): #각 행 안의 원소에서
#         found = False
#         if len(candidates)>0:
#             for idx, (value,col_idx) in enumerate(candidates): #우선 candidate에 원소가 기존에 있었는 지 체크
#                 if value == num:
#                     found = True
#                     length = j - col_idx #변의 길이 설정
#                     #업데이트
#                     candidates[idx][1] = j
#                     #사각형이 있니?
#                     if i+length<N and classs[i+length][col_idx] == classs[i+length][j] == num:
#                         max_area = max(max_area, (length + 1) ** 2)
#         #없으면 그냥 캔디에 추가
#         if not found:
#             candidates.append([num,j])
            
# print(max_area)

#각 원소에 대해 매번, 사각형이 성립하는 지 확인, 성립하면 갱신

for row_idx in range(N):
    for col_idx in range(M):
        for each_num in range(1,min(N-row_idx,M-col_idx)): #오른쪽 아래로만 확인해야댐
            if(classs[row_idx][col_idx] == classs[row_idx+each_num][col_idx] and classs[row_idx][col_idx] == classs[row_idx][col_idx+each_num] and classs[row_idx][col_idx] == classs[row_idx+each_num][col_idx+each_num]):
                area = (each_num+1) **2
                max_area = max(max_area, area)


print(max_area)