n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = [1]
ans = 0
for i in range(n - 1):
    if a[i] == a[i + 1]:
        cnt[-1] += 1

    else:
        ans += (n - (i + 1)) * cnt[-1]
        cnt.append(1)

print(ans)

# 別解
# from collections import defaultdict

# n = int(input())
# A = list(map(int, input().split()))
# cnt = defaultdict(int)
# for a in A:
#     cnt[a] += 1

# ans = (n * (n - 1)) / 2  # if not duplicate
# for a in set(A):
#     ans -= (cnt[a] * (cnt[a] - 1)) / 2
# print(int(ans))
