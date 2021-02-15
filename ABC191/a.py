v, t, s, d = map(int, input().split())
if v*t > d or v*s <d:
    print('Yes')
else:
    print('No')