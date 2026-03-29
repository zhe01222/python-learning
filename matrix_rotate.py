# 1. 給定一個 2x3 的矩陣
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# 先準備一個空的「大箱子」，用來裝旋轉後的每一列
rotated_matrix = []

# 2. 開始旋轉邏輯
for row in zip(*matrix):
    # 第一圈的時候，row 會拿到 (1, 4)
    # 第二圈的時候，row 會拿到 (2, 5)
    # 第三圈的時候，row 會拿到 (3, 6)
    
    # 我們把拿到的 row 反轉，並轉換成 list
    reversed_row = list(row[::-1]) 
    
    # 把反轉後的小串列，塞進大箱子裡
    rotated_matrix.append(reversed_row)

# 3. 逐行印出結果檢查
for row in rotated_matrix:
    print(row)