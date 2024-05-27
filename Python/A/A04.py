n = int(input())
ans=[]

for i in range(9, -1, -1):
    if pow(2, i) <=n:
        n-=pow(2, i)
        ans.append(1)
    else:
        ans.append(0)

print("".join(map(str, ans)))