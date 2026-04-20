# --- 1. 準備資料與變數 ---
scores = list(map(int, input().split()))

current_combo = 0
max_combo = 0
first_miss_index = -1  # 先設定為 -1，當作「還沒失誤過」的標記

# --- 2. 開始巡視 (因為要記位置，必須拿出地圖座標 i) ---
for i in range(len(scores)):
    
    # 為了讓程式碼好讀，我們先把櫃子裡的分數拿出來放到 s 裡面
    s = scores[i]
    
    if s > 0:
        # 情況 A：拿到分數了 -> 狀態延續
        current_combo += 1
        
        # 挑戰擂台主
        if current_combo > max_combo:
            max_combo = current_combo
            
    else:
        # 情況 B：拿到 0 分了 -> 狀態中斷
        current_combo = 0
        
        # 關鍵點：如果是「第一次」拿到 0 分，就把當下的座標 i 記下來
        if first_miss_index == -1:
            first_miss_index = i

# --- 3. 輸出分析結果 ---
print(max_combo)
print(first_miss_index)

# (這段是額外加給你看的，考試時印出上面兩個數字就好)
print("--- 詳細分析報告 ---")
print(f"最大 Combo 數：{max_combo}")
if first_miss_index != -1:
    print(f"第一次斷 Combo 出現在 Index [{first_miss_index}]")
else:
    print("太神啦！整場 Full Combo 沒有斷！")