for cases in range(int(input())):
    n,m,k = list(map(int, input().split()))
    cardPerEach = n//k
    if m<= cardPerEach:
        print(m)
    else:
        remain = m - cardPerEach
        if remain%(k-1) == 0:
            print(cardPerEach - (remain//(k-1)))
        else:
            print(cardPerEach - (remain//(k-1)) -1)