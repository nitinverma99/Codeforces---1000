from types import CodeType


s = input()
lst = ['h', 'e', 'l', 'o']
gst = []
for i in range(len(s)):
    if s[i] in lst:
        gst.append(i)
    else:
        continue
print(gst)
for i in range(len(gst)-1):
    if gst[i+1] > gst[i]:
        continue
    elif i == len(gst)-2 :
        print("YES")
        break
    else:
        print("NO")
        break