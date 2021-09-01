n = int(input())
name_list = list(input() for i in range(n))

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if name_list[i] == name_list[j]:
            print("Yes")
            exit()

print("No")
