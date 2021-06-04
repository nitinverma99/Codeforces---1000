import math
n = int(input())
x = []
y = []
z = []
for cases in range(n):
    a,b,c = list(map(int, input().split()))
    x.append(a)
    y.append(b)
    z.append(c)
summ_x = sum(x)
summ_y = sum(y)
summ_z = sum(z)
if math.sqrt(summ_x**(2) + summ_y**(2) + summ_z**(2)) == 0:
    print("YES")
else:
    print("NO")