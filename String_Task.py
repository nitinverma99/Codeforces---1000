s = input().lower()
lst = ["a",'e','i','o','u','y']
gst = []
for i in range(len(s)):
    if s[i] in lst:
        continue
    else:
        gst.append('.'+s[i])
print(''.join(gst))