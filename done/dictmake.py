import sys 

N = int(sys.stdin.readline())
list = []
for _ in range(N):
    in_word = str(sys.stdin.readline().strip())
    if list.count(in_word) == 0:
        list.append(in_word)
    
sorted_list_bro = sorted(list, key=len)

for words in sorted_list_bro:
    print(words)