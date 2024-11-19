N = int(input())
limbos = list(map(int,input().split()))

success = True
for limbo in limbos:
    if limbo <= 160:
        print("I "+str(limbo))
        success = False
        break
    
if success:
    print('P')