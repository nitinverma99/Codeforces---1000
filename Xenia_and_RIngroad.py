n,m = list(map(int, input().split()))
lst = list(map(int, input().split()))
summ = lst[0] - 1
for i in range(1, m):
    if lst[i] >= lst[i-1]:
        summ += lst[i] - lst[i-1]
    else:
        summ += (n + lst[i] -lst[i-1])
print(summ)