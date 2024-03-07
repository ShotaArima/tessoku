def event_sum(a, l, r):
    sum = 0
    for i in range(l, r):
        sum += a[i]
    return sum

n, q = map(int, input().split())
a = list(map(int, input().split()))
list_l = [ None ] * q
list_r = [ None ] * q
for j in range(q):
	list_l[j], list_r[j] = map(int, input().split())

for i in range(q):
    print(event_sum(a, list_l[i]-1, list_r[i]))



 
# S = [ None ] * (N + 1)
# S[0] = 0
# for i in range(N):
# 	S[i + 1] = S[i] + A[i]
 
# for j in range(Q):
# 	print(S[R[j]] - S[L[j] - 1])