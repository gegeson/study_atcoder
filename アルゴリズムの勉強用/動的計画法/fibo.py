# 動的計画法（メモ化）することでforで回すより早くなる
def fibo(n, memo={}):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
        return memo[n]


print(fibo(500))
