n = int(input())
a = list(map(int, input().split()))
q = int(input())
l = []
r = []
for i in range(q):
    tmp1, tmp2 = map(int, input().split())
    l.append(tmp1)
    r.append(tmp2)

for i in range(1, n):
    a[i] = a[i-1] + a[i]

for i in range(q):
    if l[i] -2 < 0:
        num_win2 = 2*a[r[i] -1]
        if num_win2 == r[i]:
            ans = "draw"
        elif num_win2  > r[i]:
            ans = "win"
        elif num_win2 < r[i]:
            ans = "lose"
    else:
        num_win2 = 2*(a[r[i] -1 ] - a[l[i] - 2])
        if num_win2 == r[i]-l[i]+1:
            ans = "draw"
        elif num_win2 > r[i]-l[i]+1 :
            ans = "win"
        elif num_win2 < r[i]-l[i]+1:
            ans = "lose"
    print(ans)