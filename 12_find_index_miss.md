content = """# APCS Python 實作詳解：Combo 狀態追蹤與分析

這份筆記詳細拆解了 APCS 實作題中常見的「狀態監控」與「首斷位置」邏輯。這對於處理遊戲開發、數據統計或連續事件分析非常關鍵。

---

## 💻 完整程式碼與逐行詳解

```python
# 1. 讀取輸入的分數序列並轉換為整數清單
# map(int, ...) 會將輸入的每個字串轉為數字，list() 則將其包裝成陣列
scores = list(map(int, input().split()))

# 2. 初始化監控變數
current_combo = 0     # 追蹤「當下」的連擊狀態，Miss 時會歸零
max_combo = 0         # 記錄「整場」的最高點，只有被超越時才會更新
first_miss_index = -1 # 標記第一次失誤的位置。使用 -1 代表「尚未發生過失誤」

# 3. 走訪陣列 (使用索引流派，因為需要紀錄位置 i)
# range(len(scores)) 會產生從 0 到最後一個位置的編號
for i in range(len(scores)):
    s = scores[i]  # 取得當前第 i 個位置的分數本人
    
    if s > 0:
        # 情況 A：成功命中 (分數大於 0)
        current_combo += 1  # 連擊數增加
        
        # 挑戰擂台主：如果目前連擊超越最高紀錄，則更新紀錄
        if current_combo > max_combo:
            max_combo = current_combo
            
    else:
        # 情況 B：發生失誤 (分數為 0)
        current_combo = 0  # 連擊無情歸零
        
        # 首斷檢查：如果這是「第一次」失誤 (標記仍為預設的 -1)
        if first_miss_index == -1:
            first_miss_index = i  # 記下當下的座標 i
            # 之後再遇到 0，因為 first_miss_index 已不是 -1，就不會再跑進來

# 4. 輸出分析結果
print(max_combo)
print(first_miss_index)