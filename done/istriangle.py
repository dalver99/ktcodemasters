A,B,N= map(int,input().split())

if (N-B) % (A-B) == 0:
    print ((N-B) // (A-B))
else:
    print ((N-B) // (A-B)+1)