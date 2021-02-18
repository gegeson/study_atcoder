x, y = map(int, input().split())

if x < y:
    x += 3
    if x > y:
        print('Yes')
    else:
        print('No')
else:
    y += 3
    if x < y:
        print('Yes')
    else:
        print('No')
        