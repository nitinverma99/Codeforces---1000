n,t = list(map(int, input().split()))
lst = list(map(int, input().split()))
i = 1
while True:
    i = i+lst[i-1]
    if i == t:
        print("YES")
        break
    if i > t:
        print("NO")
        break