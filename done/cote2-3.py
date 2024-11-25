

directions = [1,2,3]
board= [[1][2]]
x=1
N=4
y=3
q = [1]
dx = 1
dy = 2


# 일단 0 가정하고
clean = True

# 그 주변에 보드 내 칸에 지뢰가 하나라도 있다면, 클린이 아님
for dx2, dy2 in directions:
    if 0<x+dx2<=N and 0<y+dy2<=N and board[x+dx2][y+dy2] == 'M':
        clean = False

# 헌대 다 통과했다면? 큐에 추가
if clean:
    q.append([x+dx, y+dy])