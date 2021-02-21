x = int(input())
m = int(input())

# dを求める
x_list = []
while x > 0:
    x_list.append(x%10)
    x //= 10
x_list.reverse()
d = max(x_list) + 1

cnt = 0
while True:
    for i in range(len(x_copy)):
        num = x[i] + i ** d
        if num <= m:
            cnt += 1
        else:
            print(cnt)
    d += 1