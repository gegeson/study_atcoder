n = int(input())
a = list(map(int, input().split()))
 
#  indexのリスト
s = [0]*200
for i in range(n):
    s[a[i]%200] += 1
 
ans = 0
for i in range(200):
    ans += (s[i]*(s[i]-1)) // 2
    
print(ans)