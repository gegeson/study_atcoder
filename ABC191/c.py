h, w = map(int, input().split())

s = []
for i in range(h):
    s.append(list(map(str, input())))

# 交点の周りの4マスで奇数個黒マスがある時、頂点になる
ans = 0
for i in range(h-1):
    for j in range(w-1):
        count = 0
        if s[i][j] == '#':
            count += 1
        if s[i][j+1] == '#':
            count += 1
        if s[i+1][j] == '#':
            count += 1
        if s[i+1][j+1] == '#':
            count += 1
            
        if count == 1 or count == 3:
            ans += 1

print(ans)