# APCS Python 衝刺筆記：for 迴圈中的變數定義

在 Python 中，`for` 迴圈的語法是 `for 變數 in 疊代物件:`。這裡的「變數」是**動態產生**的，完全不需要像 C/C++ 那樣事先宣告型別（例如 `int i;` 或 `vector<int> row;`）。

## 1. Python 的 for 迴圈是怎麼運作的？


當你寫下 `for row in zip(*matrix):` 時，Python 在背後自動幫你做了這些事：

1. **創造變數**：它當場變出了一個叫做 `row` 的變數。
2. **自動賦值（抓取）**：它會去後面的 `zip(*matrix)` 裡面，把第一個元素抓出來，裝進 `row` 裡面。
3. **執行區塊**：執行迴圈裡面的程式碼。
4. **重複動作**：進入下一圈，自動把第二個元素抓出來覆蓋掉 `row` 裡面的舊資料，直到東西被抓完為止。

### 步驟拆解範例
假設 `zip(*matrix)` 裡面有三個包裹：`(1, 4)`, `(2, 5)`, `(3, 6)`。

```python
for row in zip(*matrix):
    print(row)

# 第 1 圈：Python 自動讓 row = (1, 4)，然後執行 print(row)
# 第 2 圈：Python 自動讓 row = (2, 5)，然後執行 print(row)
# 第 3 圈：Python 自動讓 row = (3, 6)，然後執行 print(row)
# 結束迴圈！