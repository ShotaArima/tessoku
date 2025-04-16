n, q = map(int, input().split())
a = list(map(int, input().split()))
l = []
r = []
for i in range(q):
    tmp1, tmp2 = map(int, input().split())
    l.append(tmp1)
    r.append(tmp2)

for i in range(len(a)-1):
    a[i+1] = a[i] + a[i+1]

for i in range(q):
    print(a[r[i]-1]-a[l[i]-2])