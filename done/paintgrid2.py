# https://algo.monster/liteproblems/1931

# Write a recureence relation python code for me.

# This will start with 8 numbers, on 8 positions. 
# [6,6,6,6,6,6,6,6]

# On the next phase, each position spreads out on to other positions like a neural network.

# 1 > [18, 12, 12, 6, 0, 6, 12, 12]
# 2 > [12, 12, 12, 6, 6, 6, 6, 6]
# 3 > [12, 12, 12, 6, 0, 6, 12, 12]
# 4 > [6, 6, 6, 12, 6, 6, 6, 6]
# 5 > [0, 6, 0, 6, 12, 6, 0, 6]
# 6 > [6, 6, 6, 6, 6, 12, 6, 6]
# 7 > [12, 6, 12, 6, 0, 6, 12, 6]
# 8 > [12, 6, 12, 6, 6, 6, 6, 12]

# So on the second iteration, it will look like

# [18+12+12+12+6+0+6+12+12, ... ]

import numpy as np
def recurrence(V, W, n_iterations):
    W = W / 6
    V_current = V.copy()
    for i in range(n_iterations):
        V_current = W @ V_current
        print(f"After iteration {i+1}: {V_current}")
        print(int(sum(V_current)* 6))
    return V_current

V0 = np.array([1, 1, 1, 1, 1, 1, 1, 1])

#Weight
W = np.array([
    [18, 12, 12,  6,  0,  6, 12, 12],
    [12, 12, 12,  6,  6,  6,  6,  6],
    [12, 12, 12,  6,  0,  6, 12, 12],
    [ 6,  6,  6, 12,  6,  6,  6,  6],
    [ 0,  6,  0,  6, 12,  6,  0,  6],
    [ 6,  6,  6,  6,  6, 12,  6,  6],
    [12,  6, 12,  6,  0,  6, 12,  6],
    [12,  6, 12,  6,  6,  6,  6, 12]
])

n_iterations = 4
V_final = recurrence(V0, W, n_iterations)