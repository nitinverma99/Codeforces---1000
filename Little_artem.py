for cases in range(int(input())):
    n,m = list(map(int, input().split()))
    s = 'W' + ('B'*10000)
    for i in range(n):
        print(s[i:m+i])
    