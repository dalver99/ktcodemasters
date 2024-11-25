def solution(histogram):
    height = len(histogram)
    width = len(histogram[0])
    new_list = [[] for _ in range(width)]

    for i in range(height):
        for j in range(width):
            new_list[i].append(histogram[i][j])

    #now new list has it from top to bottom

    possible = []

    for each_stick in new_list:
        for idx, each_block in enumerate(each_stick):
            flag = False
            hole_stick = False
            # 0은 고려하지 않아도 됨

            # 1이 제일 먼저 나오면 경우의수는 한계 끝
            if each_block == 1:
                possible.append(1)
                break


            # 2가 제일 먼저나오면 파란색, 또는 바닥까지의 길이가 경우의 수. 근데 구멍이 있는지 확인해야함
                # 구멍이 잇으면? 끝
                # 구멍이 있으면, 특정되었음
                # 구멍이 없으면, 파란색이나 바닥까지 길이를 재야함




    for each_stick in new_list:
        flag = False
        hole_stick = False

        for idx, each_block in enumerate(each_stick):
            # 1이 제일 먼저 나오면 경우의수는 한계 끝
            if each_block == 1:
                possible.append(1)
                break

            # 2가 제일 먼저나오면 파란색, 또는 바닥까지의 길이가 경우의 수. 근데 구멍이 있는지 확인해야함
            if each_block == 2 and not flag:
                flag = True
                #구멍이 잇으면? 끝
                for k in range(idx+1, height):
                    if each_stick[k] == 0:
                        hole_stick = True
                # 구멍이 있으면, 특정되었음
                if hole_stick:
                    possible.append(1)

                # 구멍이 없으면, 파란색이나 바닥까지 길이를 재야함
                else:
                    temp_poss = 1
                    for i in range(idx+1, height):
                        if each_stick[i] == 1 or 0:
                            # 그만 세야한다
                            break

                        if each_stick[i] == 2:
                            temp_poss += 1
                    possible.append(temp_poss+1)


    answer = 1
    for each_poss in possible:
        answer *= each_poss
    return answer