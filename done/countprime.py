def isprime(n):
    isprimenum = True
    for i in range (2,n-1):
        if n%i == 0:
            isprimenum = False
        
    return isprimenum
    
N = int(input())
count= 0
for a in range(2,N):
    if(isprime(a)):
        count += 1

print(count)