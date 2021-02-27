n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

x = []
for i in range(len(a)):
    if a[i][2] - a[i][0] > 0:
        x.append(a[i][1])
if x:
    print(min(x))
else:
    print(-1)