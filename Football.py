lst = []
for cases in range(int(input())):
    k = input()
    lst.append(k)
sett = set(lst)
sett = list(sett)
maxx = {}
for i in range(len(sett)):
    maxx[sett[i]] = lst.count(sett[i])
maxx = {value:key for key,value in maxx.items()}
keys = maxx.keys()
print(maxx[max(keys)])