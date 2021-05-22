from operator import mul

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_index = [0 for i in range(n)]
a_count = [0 for i in range(n)]
for i in range(n):
    a_index[b[c[i] - 1] - 1] += 1
    a_count[a[i] - 1] += 1 

combined = map(mul, a_count, a_index)

print(sum(combined))