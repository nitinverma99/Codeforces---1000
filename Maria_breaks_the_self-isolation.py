for cases in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    count = n+1
    lst.sort()
    for i in range(n-1, -1, -1):
        if lst[i] > count-1:
            count -= 1
        else:
            continue
    print(count)