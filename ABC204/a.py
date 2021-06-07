x, y = map(int, input().split())
num_list = [0, 1, 2]
if x == y:
    print(x)
else:
    num_list.remove(x)
    num_list.remove(y)
    print(num_list[0])
    
