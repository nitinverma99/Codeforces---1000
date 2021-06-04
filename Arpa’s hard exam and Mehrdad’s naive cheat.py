n = int(input())
if n == 0:
    print('1')
else:
    remain = n%4 
    if remain == 1:
        print('8')
    elif remain == 2:
        print('4')
    elif remain == 3:
        print('2')
    elif remain == 0:
        print('6')