n, t = list(map(int, input().split()))
if n ==1:
    if t == 10:
        print('-1')
    else:
        print(t)
elif t<10:
    print(str(t)*n)
else:
    print('1'+('0'*(n-1)))