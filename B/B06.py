n = int(input())
a = list(map(int, input().split()))
q = int(input())
l = []
r = []
for i in range(q):
    l_val, r_val = map(int, input().split())
    l.append(l_val)
    r.append(r_val)
num = []
for i in range(n):
    if i == 0:
        num.append(a[i])
    else:
        num.append(a[i] + num[i - 1])

for i in range(q):
    if l[i]-2 < 0:
        ans = num[r[i]-1]
    else:
        ans = num[r[i]-1]-num[l[i]-2]
    # print(ans) # あたりの数がans, 総回数がr[i]-l[i]+1
    count = r[i]-l[i]+1-ans
    if ans > count:
        print("win")
    elif ans == count:
        print("draw")
    else:
        print("lose")
