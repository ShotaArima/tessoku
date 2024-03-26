n, q = map(int, input().split())
a = list(map(int, input().split()))
num = []
# print("n: ", n)
# print("q: ", q)
# print("a: ", a)
num.append(a[0])
for i in range(1, n):
    num.append(a[i] + num[i - 1])
# print("num: ", num)
l = []
r = []
for i in range(q):
    l_val, r_val = map(int, input().split())
    l.append(l_val)
    r.append(r_val)

for i in range(q):
    # print(f"{num[r[i]-1]}-{num[l[i]-2]}")
    if l[i]-2 < 0:
        ans = num[r[i]-1]
    else:
        ans = num[r[i]-1]-num[l[i]-2]
    print(ans)

