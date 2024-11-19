from itertools import combinations
from copy import deepcopy
from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#super standard bgf
def bfs(wheres_jaguar, grid, N, M):
    visited = [[False] * M for _ in range(N)]
    queue = deque(wheres_jaguar)
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx,ny = x + dx, y +dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    safe_count = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0 and not visited[i][j]:
                safe_count += 1
    return safe_count

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

empty_spots = []
wheres_jaguar = []

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            empty_spots.append((i, j))
        elif grid[i][j] == 2:
            wheres_jaguar.append((i, j))

max_safe_area = 0

# 3벽이를 다 조합해서 던져보기
for walls in combinations(empty_spots, 3):
    temp_grid = deepcopy(grid)
    for wx, wy in walls:
        temp_grid[wx][wy] = 1
    
    safe_area = bfs(wheres_jaguar, temp_grid, N, M)
    max_safe_area = max(max_safe_area, safe_area)

    for wx, wy in walls:
        grid[wx][wy] = 0

print(max_safe_area)