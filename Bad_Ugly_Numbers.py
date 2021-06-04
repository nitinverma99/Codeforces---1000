for cases in range(int(input())):
    n = int(input())
    if n == 1:
        print('-1')
    else:
        s = '2' + ('4' * 100000)
        print(s[0:n-1] + '9')