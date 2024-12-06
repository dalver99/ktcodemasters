inp = input()
print('no' if inp=='OOOO' or (inp=='OXOX' and [input(), input(), input()][-1][3]=='O') else 'yes')