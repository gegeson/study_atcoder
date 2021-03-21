n = int(input())
a = 1
while True:
    if (n // (1000 ** a)) > 1000:
        a += 1
    else:
        break
    
ans = 0
if a >= 2:
    for i in range(1, a):
        print(i)
        ans += 999 * (1000 ** i)
ans += (n % (1000 ** a)) + 1
print(ans)
