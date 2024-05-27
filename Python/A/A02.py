# NとXを受け取る
N, X = map(int, input().split())

# A_1からA_Nまでの要素を受け取る
A_list = list(map(int, input().split()))

# # 入力内容を表示（確認用）
# print("N:", N)
# print("X:", X)
# print("A_list:", A_list)

for i in range(N):
    if A_list[i] == X:
        print("Yes")
        break
else:
    print("No")