n = int(input())
ss = set(input() for i in range(n))
for s in ss:
    if "!" + s in ss:
        print(s)
        exit()
print("satisfiable")