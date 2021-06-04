for cases in range(int(input())):
    n = int(input())
    # middle = (n//2) + 1
    # count = 0
    # for i in range(1, n+1):
    #     if i< middle:
    #         for j in range(n):
    #             count += middle - min(i,j)
    #     elif i == middle :
    #         for j in range(n):
    #             count += abs(middle- j)
    #     elif i> middle:
    #         for j in range(n):
    #             count+= max(i,j) - middle
    # print(count)
    count = 0
    for i in range(1, n//2 + 1):
        count += 8*i*i
    print(count)
