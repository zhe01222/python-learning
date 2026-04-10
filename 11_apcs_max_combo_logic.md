# APCS Python 核心邏輯：狀態追蹤與最大值更新 (Max Combo 機制)

在處理遊戲計分、連續事件（如：最長連續登入天數、最大連擊數）時，我們不需要記住整個陣列的位置，只需要掌握「當下狀態」與「歷史最高」的關係。

---

## ⚔️ 核心觀念一：變數的「雙軌制」
要計算最大 Combo，我們腦袋裡（和程式裡）必須同時維持兩個變數，它們各司其職：

1. **`current_combo` (現在的 Combo)：**
   * **角色：** 負責記錄「當下的狀態」。
   * **特性：** 隨著遊戲進行會增加，但也隨時有可能因為失誤（拿到 0 分）而**歸零**。
2. **`max_combo` (歷史最大 Combo)：**
   * **角色：** 負責記錄整場遊戲的「最高點」。
   * **特性：** 像是一個高高在上的擂台主。它**永遠不會歸零**，只會被更大的 `current_combo` 取代。

---

## 🧠 核心觀念二：迴圈內的邏輯判斷 (if / else)
在迴圈走訪陣列（使用 `for s in scores:` 流派）時，對於每一顆音符 `s`，我們只做兩件事：

### 情況 A：拿到分數了 (s > 0)
1. **Combo 增加：** `current_combo += 1`
2. **挑戰擂台主：** 這是最重要的防線！每次 Combo 增加後，都要立刻問：「現在的 Combo 有沒有超越歷史最大值？」
   * `if current_combo > max_combo:`
       * 如果有，擂台主換人當：`max_combo = current_combo`

### 情況 B：失誤了 (s == 0)
1. **Combo 斷掉：** 直接無情歸零 `current_combo = 0`。
   * *(注意：這裡不需要動到 `max_combo`，因為歷史最高紀錄不會因為你現在斷線就消失。)*

---

## 💻 標準實作碼 (起手式模板)

這是一段可以套用在所有「尋找最長連續狀態」題型的標準模板：

```python
scores = [300, 100, 300, 0, 300, 300, 300, 0, 100]

current_combo = 0   # 記錄現在的連擊
max_combo = 0       # 記錄歷史的最高

for s in scores:
    if s > 0:
        current_combo += 1           # 狀態延續：連擊 +1
        if current_combo > max_combo:
            max_combo = current_combo # 打擂台：破紀錄了就更新
    else:
        current_combo = 0            # 狀態中斷：直接歸零

print(f"這場遊戲的最大 Combo 數為：{max_combo}")