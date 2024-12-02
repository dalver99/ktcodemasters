N  = 5
board = [ ([0] * (N+1)) for _ in range (N+1)]

print(board)

mine = [[1,2],[2,3]]

for each_mine in mine:
    board[each_mine[0]][each_mine[1]] = 'M'

