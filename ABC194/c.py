# これだとO(N2)で間に合わない
# n = int(input())
# a_list = tuple(map(int, input().split()))

# ans = 0 
# for i in range(0, n-1):
#     for j in range(i, n):
#         sum = (a_list[i] - a_list[j]) ** 2
#         ans += sum
# print(ans)


N = int(input())
A = list(map(int, input().split()))
counts = [0] * 401
# あの要素で同じものを数え上げる
for a in A:
    counts[a + 200] += 1

ans = 0
for i in range(-200, 201):
    for j in range(-200, 201):
        if i == j:
            continue
        count_i = counts[i + 200]
        count_j = counts[j + 200]
        if count_i == 0 or count_j == 0:
            continue
        ans += count_i * count_j * abs(i - j)**2
print(ans // 2)