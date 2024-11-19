#print(ord('a')) #97
#print(chr(97)) #65
#알파벳 26개

strung = input()
strung = strung.lower()

ans = 'YES'
for i in range (26):
    #알파벳 소문자 a부터 z가 들어있는지 확인
    #A부터 Z가 있는지 확인
    if (chr(97+i)) not in strung:
        ans = 'NO'
        break

print(ans)
