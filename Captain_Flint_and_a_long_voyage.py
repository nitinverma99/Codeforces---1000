import math
for cases in range(int(input())):
    n = int(input())
    if n == 1:
        print('8')
    else:
        remain = math.ceil(n/4)
        print('9'*(n-remain) + '8'*remain)