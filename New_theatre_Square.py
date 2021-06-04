for cases in range(int(input())):
    n,m,x,y = list(map(int, input().split()))
    minn = min([(2*x), y])
    count = 0
    for i in range(n):
        s = input()        
        count1 = s.count('..')
        count2 = s.count('.') - 2*count1
        count += count1*minn + count2*x
    print(count)