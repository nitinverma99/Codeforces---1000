s,n = list(map(int, input().split()))
lst = []
for cases in range(n):
    a,b = list(map(int, input().split()))
    lst.append([a,b])
lst.sort(key= lambda x: x[0])
for i in range(n):
    if s> lst[i][0]:
        s += lst[i][1]
        if i == n-1:
            print("YES")
            break
    else:
        print("NO")
        break
