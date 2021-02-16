n, x = map(int, input().split())

# 浮動小数点の計算を避けるために*100をする
alc = 0
count = 0
for i in range(n):
    v, p = map(int, input().split())
    alc += v * p
    count += 1
    if alc > x * 100:
        print(count)
        exit()

if alc <= x * 100:
    print(-1)