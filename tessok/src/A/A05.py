n, k = map(int, input().split())
count = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        z = k - (x+y)
        if 1 <= z & z <= n:
            count +=1
print(count)