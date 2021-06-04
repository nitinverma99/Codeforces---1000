n,a,b = list(map(int, input().split()))
remain = n -a -b
if remain>1:
    print(n- a - remain +1)
else:
    print(n-a)