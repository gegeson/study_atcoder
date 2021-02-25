n = int(input())
xy = [tuple(map(int, input().split())) for i in range(n)]
cnt = 0

for i in range(n-1):
    for j in range(i+1, n):
        if xy[j][0] - xy[i][0] == 0:
            continue
        ans = (xy[j][1]- xy[i][1]) / (xy[j][0] - xy[i][0])
        if -1 <= ans <= 1:
            cnt += 1
print(cnt)
    