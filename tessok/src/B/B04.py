n = input()  # 文字列として受け取る
ans = 0
for i, digit in enumerate(reversed(n)):
    print(digit)
    if digit == '1':
        ans += 2 ** i
print(ans)

# print(int(input(), 2))  # 入力を2進数として扱い、そのままint変換
