n = int(input())
a = list(map(int, input().split()))
 
ans = 0
 
for i in range(n):
    min_a = a[i]
    for j in range(i, n):
        min_a = min(min_a, a[j])
        num = min_a * (j-i+1)
        ans = max(ans, num)
 
print(ans)