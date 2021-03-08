n = int(input())
a_list = []
b_list = []
for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

ans = 100000000
for i in range(n):
    for j in range(n):
        ans = min(ans, a_list[i] + b_list[j] if i == j else max(a_list[i], b_list[j]))
print(ans)