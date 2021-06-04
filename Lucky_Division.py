lst= [4,7,44,47,74,77,444,447,474,477,747,774,777]
s = input()
if (s.count('4') + s.count('7')) == len(s):
    print("YES")
else:
    s = int(s)
    for i in range(len(lst)):
        if s%lst[i] == 0:
            print("YES")
            break
        elif i == len(lst) - 1 :
            print("NO")