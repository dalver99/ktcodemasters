time = input()
N = int(input())

hr = int(time[0:2])
min = int(time[3:5])

current = hr*60 + min
sum = (((N)*(N-1))//2)
result = (current+sum)%1440
#print(result)
nhr = int(result//60)
nmin = int(result%60)
#print(nhr,nmin)
shr = str((nhr))
smin = str((nmin))

shr = shr.zfill(2)
smin = smin.zfill(2)

print(shr + ':' + smin)