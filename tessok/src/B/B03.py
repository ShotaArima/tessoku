n = int(input())
a = list(map(int, input().split()))

ans = "No"
for i in range(n):
    for j in range(n):
        for k in range(n):
            if (i==j) | (j==k) | (k==i):
                break
            if a[i] + a[j] + a[k] == 1000:
                ans = "Yes"
print(ans)