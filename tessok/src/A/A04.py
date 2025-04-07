n = int(input())
for i in range(9, -1, -1):
    print((n >> i) & 1, end="") # n>>i でビットシフトし、 &1　で下位1ビットを取得、end=""で改行空白なしで出力
print()