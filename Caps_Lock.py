s = input()
mm = 0
for i in range(1, len(s)):
    if ord(s[i]) >64 and ord(s[i]) <97 :
        mm+=1
    else:
        break
if mm == len(s) -1:
    print(s.swapcase())
else:
    print(s)
    