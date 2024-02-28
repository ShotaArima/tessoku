n, k = map(int, input().split())
count=0

for i in range(1, n+1):
    for j in range(1, n+1):
        w=k-j-i
        if w>0 and w<=n:
            # print("Yes")
            count+=1
            # print(i, j, w)

print(count)