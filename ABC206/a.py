n = int(input())

res = int(n * 1.08)

if res < 206:
    print('Yay!')
elif res == 206:
    print('so-so')
else:
    print(':(')