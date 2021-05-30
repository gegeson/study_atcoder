import statistics


n, k = map(int, input().split())
a = [list(map(int,input().split())) for i in range(n)]
median_list = []

for i in range(n-k+1):
    for j in range(n-k+1):
        suq = []
        for l in range(i, i+k):
            for m in range(j, j+k):
                suq.append(a[l][m])
        suq.sort()
        print(suq)
        if len(suq) % 2 == 1:  
            median_list.append(statistics.median(suq))
        else:
            index, mod = divmod(k * k, 2)
            median_list.append(suq[index])

median_list.sort()
print(int(median_list[0]))