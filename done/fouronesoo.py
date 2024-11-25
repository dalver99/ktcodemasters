import sys
input = sys.stdin.readline

a1,b1,c1,d1 = map(int,input().strip().split())
a2,b2,c2,d2 = map(int,input().strip().split())

i = (a1*b2) + (a2*b1) + (c1*d2) - (d1*c2)
j = (a2*c1) + (a1*c2) - (b1*d2) - (d1*b2)
k = (a2*d1) + (a1*d2) - (c1*b2) + (b1*c2)
w = a1*a2 - b1*b2 - c1*c2 - d1*d2

print(f'{w} {i} {j} {k}') 