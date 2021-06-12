N = int(input())
#Sはリストとして保管したい。
S = list(input())
Q = int(input())
#print(S)

t = False
for i in range(Q):
    T,A,B = map(int,input().split())
    if T == 1:   
        if t:
            #文字変換
            if A > N:
                A -= N
            else :
                A += N
            if B > N:
                B -= N
            else :
                B += N
        w = S[B-1]
        S[B-1] = S[A-1]
        S[A-1] = w
    else:
        t = not t

if t:
    temp = S[N:]
    S[N:] = S[:N]
    S[:N] = temp
print("".join(S))