N, K = map(int,input().split())
string = input()
result = ''
for i in string:
    result += i*K
print(result)