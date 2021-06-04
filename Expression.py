a = int(input())
b = int(input())
c = int(input())
first = a+b+c
second = (a+b)*c
third = a*(b+c)
fourth = a*b*c
print(max([first, second, third, fourth]))