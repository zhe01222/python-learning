secret_codes = ["rets@mlodI", "YNHS", "uso"]

# 請在下方寫下你的解碼邏輯：
decoded_codes =[code[::-1] for code in secret_codes]
print(decoded_codes)