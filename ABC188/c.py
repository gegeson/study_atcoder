n = int(input())
a = list(map(int, input().split()))
 
n = 2**n
l = a[:n//2]
r = a[n//2:]
print(a.index(min(max(l), max(r)))+1)