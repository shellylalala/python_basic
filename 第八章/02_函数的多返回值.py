def calculate(x, y):
    res1 = x + y
    res2 = x - y
    return res1, res2  # 元组形式返回


res = calculate(1, 2)
r1, r2 = calculate(1, 2)

print(res)  # (3, -1)
print(r1)  # 3
print(r2)  # -1
