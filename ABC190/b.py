n, s, d = map(int, input().split())

count = 0
for i in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
        count += 1
        
if  count > 0:
    print('Yes')
else:
    print('No')