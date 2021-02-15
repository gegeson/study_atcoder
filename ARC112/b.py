b, c = map(int, input().split())

if c == 1:
    if b == 0:print(1)
    else:print(2)
    exit()
    
# 取りうる値の範囲を調べる
if b > 0:
    x1 = b + (c - 2) // 2
    x2 = max(0, b - c // 2)
    x3 = min(-1, -b + (c - 1) // 2)
    x4 = -b - (c - 1) // 2
else:
    x1 = -b + (c - 1) // 2
    x2 = max(0, -b - (c - 1) // 2)
    x3 = min(-1, b + (c - 2) // 2)
    x4 = b - c // 2

print(x1 - x2 + x3 - x4 + 2)
    
    