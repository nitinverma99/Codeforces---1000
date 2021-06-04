for cases in range(int(input())):
    a,b,n,S = list(map(int, input().split()))
    remain = S%n
    if remain <= b and (a*n + b) >= S:
        print("YES")
    else:
        print("NO")