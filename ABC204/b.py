n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i] <= 10:
        pass
    else:
        cnt += a[i] - 10

print(cnt)