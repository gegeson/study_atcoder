# ACB057C
n = int(input())
m = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        a = int(n / i)
        m.append(max(len(str(i)), len(str(a))))

print(min(m))
