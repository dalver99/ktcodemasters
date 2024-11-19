N = int(input())
five = N%5
seven = N%7

if five < seven:
    print(seven)
else:
    print(five)