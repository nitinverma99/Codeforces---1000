dictt = {}
n,m = list(map(int, input().split()))
for i in range(m):
    s = input().split()
    dictt[s[0]] = s[1]
gst = input().split()
mst = []
for i in range(n):
    if gst[i] in dictt.keys():
        len1 = len(gst[i])
        len2 = len(dictt[gst[i]])
        if len1 == len2 or len1<len2 :
            print(gst[i], end=" ")
        else:
            print(dictt[gst[i]], end=" ")
