# def convert2Binary(n):
#     res = ""

#     while n > 0:
#         if (n % 2 == 1):
#             res += '1'
#         else:
#             res += '0'
#         n = n//2
#     return res[::-1]

def convert2Binary(n):
    res = []

    while n > 0:
        res.append(str(n%2))
        n = n//2

    return ''.join(res[::-1])

n = 13
print(convert2Binary(n))
