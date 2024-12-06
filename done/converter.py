def translate(text, rule):
    if rule == 'G':
        rule_dict = {'G':'R', 'R':'B', 'B':'G'}
    elif rule == 'B':
        rule_dict = {'B':'R', 'R':'G', 'G':'B'}
    test = ' '.join([rule_dict[c] for c in text.split()])
    if test == 'R G R G R' or test == 'R B R B R':
        test = 1
    if test == 'R G R G B' or test == 'R B R B G':
        test = 2
    if test == 'R G R B R' or test == 'R B R G R':
        test = 3
    if test == 'R G R B G' or test == 'R B R G B':
        test = 4
    if test == 'R G B R G' or test == 'R B G R B':
        test = 5
    if test == 'R G B R B' or test == 'R B G R G':
        test = 6
    if test == 'R G B G R' or test == 'R B G B R':
        test = 7
    if test == 'R G B G B' or test == 'R B G B G':
        test = 8
    return test

def main():
    texts = '''G R G B R
G B R G R
G B R G B
G B R B R
G B G B R
B R G B R'''

    texts = texts.split('\n')
    for text in texts:
        rule = text[0]
        print(translate(text, rule))

if __name__ == "__main__":
    main()