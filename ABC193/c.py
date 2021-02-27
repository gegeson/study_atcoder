import math


n = int(input())
num_list = []
for i in range(2, int(math.sqrt(n))+1):
    for j in range(2, int(math.log(n, i))+1):
        num = i ** j
        if num <= n:
            num_list.append(num)
            
print(n - len(set(num_list)))        