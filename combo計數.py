scores = list(map(int, input().split()))

current_combo = 0
max_combo = 0

# 2. 開始巡視分數 (利用流派二：直接拿分數本人)
for s in scores:
    if s > 0:
        # 如果不是 0，Combo 增加
        current_combo += 1
        # 更新最大紀錄 (可以用 max 函式或是另一個 if)
        if current_combo > max_combo:
            max_combo = current_combo
    else:
        # 如果是 0，Combo 斷掉重算
        current_combo = 0

# 3. 印出最後結果
print(max_combo)