N = int(input())
full = []
for index in range (N):
    name,iq = map(str,input().split())
    iq = int(iq)
    full.append((iq,name,index))

sorted_full = sorted(full, key=lambda x: (-x[0], x[2]))

for stuff in sorted_full[:3]:
    print(stuff[1])