dooduhgee = []

for _ in range(8):
    row = list(str(input().strip()))
    dooduhgee.append(row)

#print(dooduhgee)

kill = 0

switch = True

for each_row in dooduhgee:
    switch = not switch
    # print(int(switch))
    for idx,each_kan in enumerate(each_row):
        if idx%2 == int(switch) and each_kan == 'F':
            kill += 1

print(kill)