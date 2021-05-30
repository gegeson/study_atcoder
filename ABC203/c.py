n, k = map(int, input().split())
p = [list(map(int,input().split())) for i in range(n)]
p.sort()
# print(p)

for i in range(n):
    if p[i][0] <= k:
        # print(p[i][0])
        k += p[i][1]
    else:
        print(k)
        exit()
    
print(k)