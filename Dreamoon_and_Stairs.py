n, m = list(map(int, input().split()))
if n< m:
    print('-1')
else:
    if n%2 == 0:
        for i in range((n//2), n+1):
            if i%m == 0:
                print(i)
                break
            elif i == n:
                print('-1')
                break
    else:
        for i in range((n//2)+1, n+1):
            if i%m == 0:
                print(i)
                break
            elif i == n:
                print('-1')
                break