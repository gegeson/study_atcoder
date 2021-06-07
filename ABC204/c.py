# 再帰回数上限変更
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
g = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    
def dfs(l):
    if n_list[l]:
        return  
    n_list[l] = True
    for ll in g[l]:
        dfs(ll)
        
ans = 0

for i in range(n):
    n_list = [False]*n
    dfs(i)
    ans += sum(n_list)
    
print(ans)