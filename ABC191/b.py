n, x = map(int, input().split())
a_list = list(map(int, input().split()))
l = []
for a in a_list:
    if a == x:
        pass
    
    else:
        l.append(a)
 
 
print(' '.join(map(str, l)))