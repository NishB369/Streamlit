n=int(input('Enter a number:'))
for i in range(n+1):
    for j in range(1,6-i):
        if j%2==0:
            print('O',end=' ')
        else:
            print('X',end=' ')
    print()