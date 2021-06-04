a,b = list(map(int, input().split()))
# print(a + (a-1)//(b-1))
total = a
left = 0
while(a>=b):
    total += a//b
    a = a//b + a%b
print(total)