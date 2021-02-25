import math

k = int(input())

cnt = 0
for i in range(1,k+1):
    for j in range(1, math.floor(k / i) + 1):
        for l in range(1, math.floor(k / i / j) + 1):
            if i * j * l <= k:
                cnt += 1
print(cnt)
        
        