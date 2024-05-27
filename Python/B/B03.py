n = int(input())
a = list(map(int, input().split()))
ans=False

for i in range(n):
    for j in range(n):
        if i==j:
            continue
        for k in range(n):
            if k==i or k==j:
                continue
            sum = a[i]+a[j]+a[k]
            if sum==1000:
                ans=True
                break

if ans:
    print("Yes")
else:  
    print("No")