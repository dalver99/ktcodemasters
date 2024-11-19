sentence = input()
sentence = sentence.lower()
s = list(set(sentence))

pengram = []
for i in range(97,123):
    pengram.append(chr(i))
    
if sorted(s) == pengram:
    print("YES")
else:
    print("NO")