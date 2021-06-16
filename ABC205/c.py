a, b, c = map(int, input().split())

if a == b:
    print('=')

elif c % 2 == 0:
    if abs(a) < abs(b):
        print('<')
    elif abs(a) == abs(b):
        print('=')
    else:
        print('>')
            
else:
    if a == 0:
        if b > 0:
            print('<')
        elif b < 0:
            print('>')
    elif b == 0:
        if a > 0:
            print('>')
        elif a < 0:
            print('<')
    elif a > 0 and b > 0:
        if a > b:
            print('>')
        elif a < b:
            print('<')
    else:
        if a < b:
            print('<')
        elif a > b:
            print('>') 