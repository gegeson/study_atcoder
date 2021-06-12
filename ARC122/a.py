n = int(input())
a = list(list(map(int, input().split())))
mod = 10**9 + 7

dp = [[0]*2 for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    dp[i+1][0] = (dp[i][0] + dp[i][1]) % mod
    dp[i+1][1] = dp[i][0] % mod
        