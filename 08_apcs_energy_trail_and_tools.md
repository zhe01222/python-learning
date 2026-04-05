# APCS Python 基礎練習與開發者裝備庫

這份筆記記錄了 APCS 實作題第 2 級分的陣列走訪練習，以及跨越程式初學者「空白畫面恐懼症」的實用工具與心法。

---

## 📝 Part 1：實作練習 - 數字步道收集能量

**【問題描述】**
角色走在一條由數字組成的步道上。每往前走一步，如果「下一步的數字」大於「現在踩著的數字」（上坡），就可以收集到等於「兩個數字差值」的能量。請計算走完步道後，總共收集了多少能量。

**【範例測試】**
* **輸入：** `1 4 2 5 3 8`
* **輸出：** `11` (過程：3 + 0 + 3 + 0 + 5 = 11)

**【實作程式碼 (AC 版)】**
成功運用 `for` 迴圈搭配 `i` 與 `i+1` 進行前後元素比較，並加入了 `len(trail) - 1` 的防呆機制，避免陣列越界 (IndexError)。

```python
# 1. 讀取使用者輸入的一整排數字，變成一個陣列
trail = list(map(int, input().split()))

# 2. 準備一個「能量收集罐」，一開始是空的
total_energy = 0

# 3. 開始走訪陣列 (跑到倒數第二個數字停下，避免 i+1 踩空)
for i in range(len(trail) - 1):
    
    current_step = trail[i]     # 現在踩著的數字
    next_step = trail[i+1]      # 下一步的數字
    
    # 4. 判斷與收集：如果是上坡
    if next_step > current_step:
        # 計算這一步收集到的能量差值
        gained = next_step - current_step
        
        # 把收集到的能量裝進罐子裡
        total_energy = total_energy + gained

# 5. 輸出總能量
print(total_energy)