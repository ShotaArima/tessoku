d = int(input())
n = int(input())
participants = [0]*(d)
for _ in range(n):
    l_val, r_val = map(int, input().split())
    participants[l_val-1] += 1
    if r_val < d:
        participants[r_val] -= 1

# print(participants)
sum_list = []
sum_list.append(participants[0])
for i in range(1, len(participants)):
    sum_list.append(sum_list[i-1]+participants[i])
print(" ".join(map(str, sum_list)))