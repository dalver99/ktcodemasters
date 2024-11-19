N,M = map(int,input().split())
ints = list(map(int,input().split()))

def transformers(n, q):
    if n == 0:
        return '0'
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        if mod > 9:
            mod = 'a'
        rev_base += str(mod)
    #뒤집어서 반납
    return rev_base[::-1] 


# def transformer(n, q):
#     if n == 0:
#         return '0'
    
#     rev_base = '' #변환된 수열을 여기에 저장
#     quo = n
#     while quo > 0:
#         rem = quo % q  # 123%10 = 3
#         quo = quo // q # 123//10 = 12
#         if rem > 9:
#             rem = 'a'
#         rev_base += str(rem)

#     #뒤집어서 반납
#     return rev_base[::-1] 

# print(transformer(123,11))

# ans = 10
# len_sum = 0
# dig = 11

# #일단 함 체크
# for each_int in ints:
#     len_sum += len(str(each_int))
# len_sum += (len(ints) - 1)

# while len_sum > M and ans < 63:
    
#     len_sum = 0
#     new_ints = []

#     for each_int in ints:
#         transformed = transformers(each_int,dig)
#         new_ints.append(transformed)

#     for each_int in new_ints:
#         len_sum += len(each_int)
#     len_sum += (len(new_ints) - 1)

#     # print(new_ints)
#     ans = dig
#     dig += 1

# if ans > 62:
#     print('-1')
# else:
#     print(ans)

