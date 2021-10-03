import itertools


n = list(map(int, input()))

max = 0
num_len = len(n) // 2
for pair in itertools.permutations(n, len(n)):
    a = list(pair)[:num_len]
    b = list(pair)[num_len:]
    a = int("".join(str(num_a) for num_a in a))
    b = int("".join(str(num_b) for num_b in b))
    if max < a * b:
        max = a * b

print(max)
