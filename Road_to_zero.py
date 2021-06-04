for cases in range(int(input())):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    case1 = min(x,y)*b + abs(x-y)*a
    case2 = max(x,y)*b + abs(x-y)*a
    case3 = x*a + y*a
    print(min([case1, case2, case3]))