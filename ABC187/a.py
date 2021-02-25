a, b = map(str, input().split())
a_sum = 0
for i in range(len(a)):
    a_sum += int(a[i])
    
b_sum = 0
for i in range(len(b)):
    b_sum += int(b[i])

max_num = max(a_sum, b_sum)
print(max_num)