from collections import deque

def search(N):
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        directions = [[1, -1], [1, 0], [1, 1], [0, -1], [0, 1], [-1, -1], [-1, 0], [-1, 1]]
        for dx, dy in directions:
            if 0 < x + dx <= N and 0 < y + dy <= N and not visited[x + dx][y + dy] and board[x + dx][y + dy] != 'M':
                # 일단 가정하고
                clean = True
                # 그 주변에 보드 내 칸에 지뢰가 하나라도 있다면, 클린이 아님
                for dx2, dy2 in directions:
                    if 0 < x + dx2 <= N and 0 < y + dy2 <= N and board[x + dx2][y + dy2] == 'M':
                        clean = False
                # 헌대 다 통과했다면? 큐에 추가
                if clean:
                    q.append([x + dx, y + dy])
    # print(visited)

    result = 0
    for row in visited:
        result += row.count(1)
    return result

def solution(N, mine, P):
    global board
    global visited
    global q
    board = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    
    for each_mine in mine:
        board[each_mine[0]][each_mine[1]] = 'M'
    # 시작은 무조건 0,0인 곳이 주어진다고 했음.
    q = [[P[0], P[1]]]
    res = search(N)
    answer = res
    return answer