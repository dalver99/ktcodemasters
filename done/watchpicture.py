greem = []
for _ in range (4):
    greem.append(list(input()))

#print(greem)
able = False
for x in range (3):
    for y in range (3):
        box = []
        for xx in range(2):
            for yy in range(2):
                box.append(greem[xx+x][yy+y])
        #print(box)
        if box.count('X') == 3 or box.count('X')==4:
            able = True


if able:
    print('yes')
else:
    print('no')