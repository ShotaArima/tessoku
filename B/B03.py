n = int(input())
a = list(map(int, input().split()))
ans=False

for i in range(n):
    for j in range(n):
        for k in range(n):
            sum = a[i]+a[j]+a[k]
            if sum==1000:
                ans=True
                break

if ans:
    print("Yes")
else:  
    print("No")