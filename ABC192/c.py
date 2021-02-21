n, k = map(int, input().split())

if k == 0:
    print(n)
    exit()
elif n == 0:
    print(0)
    exit()
    
for i in range(k):
    max_num = int(''.join(sorted(str(n), reverse = True)))
    min_num = int(''.join(sorted(str(n))))
    f = max_num - min_num
    f_copy = max_num - min_num
    n = f_copy
    
print(f)
