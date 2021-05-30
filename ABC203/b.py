n, k = map(int, input().split())

num = []
for i in range(1, n+1):
    for j in range(1, k+1):
        a = int(str(i) + '0' + str(j))
        # print(a)
        num.append(a)

print(sum(num)) 