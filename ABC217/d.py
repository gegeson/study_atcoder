import bisect
import array

l, q = map(int, input().split())
query = list(list(map(int, input().split())) for i in range(q))
p = array.array("i", [0, l])

for i in range(q):
    c, x = query[i][0], query[i][1]
    if c == 1:
        bisect.insort(p, x)
    else:
        j = bisect.bisect(p, x)
        print(p[j] - p[j - 1])
