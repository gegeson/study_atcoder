# ABC095C
a, b, c, x, y = map(int, input().split())

if a + b >= 2 * c:
    if x >= y:
        if a >= 2 * c:
            print("")
else:
    print(x * a + y * b)
