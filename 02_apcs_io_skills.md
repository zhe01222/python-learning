# APCS Python 衝刺筆記：必備的輸入輸出 (I/O) 技巧

在 APCS 實作題中，測資通常會是一整行用空格隔開的數字，或者多行輸入。Python 讀取測資的核心神技是 `input().split()` 加上 `map()`。

## 1. 讀取單行、多個用空格隔開的整數
這是 APCS 最常見的輸入格式。例如測資給：`10 20 30`

```python
# 寫法一：用 map 轉換後轉成 list (最常用於陣列)
nums = list(map(int, input().split()))
print(nums)  # 輸出：[10, 20, 30]

# 寫法二：如果確定只有兩個或三個變數，可以直接解包 (Unpacking)
a, b, c = map(int, input().split())
print(a) # 輸出：10