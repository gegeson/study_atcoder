a, b, c = map(int, input().split())

if a > b:
    print('Takahashi')
elif a < b:
    print('Aoki')
else:
    if c == 0:
        print('Aoki')
    if c == 1:
        print('Takahashi')