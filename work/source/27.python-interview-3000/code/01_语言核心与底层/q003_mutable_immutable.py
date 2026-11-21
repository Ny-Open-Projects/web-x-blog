t = ([1, 2], "abc")
t[0].append(3)     # tuple 本身没变,但它引用的 list 变了
print(t)           # ([1, 2, 3], 'abc')

try:
    d = {t: "ok"}  # 报 TypeError:tuple 的哈希按元素实时计算,装了 list 就不可哈希
except TypeError as e:
    print("unhashable:", e)

d2 = {(1, 2, "abc"): "ok"}   # 元素全不可变的 tuple 才能做 key
print(d2[(1, 2, "abc")])

def add_item(lst=[]):        # 经典陷阱:默认参数只创建一次
    lst.append(1)
    return lst

print(add_item())  # [1]
print(add_item())  # [1, 1]

if __name__ == "__main__":
    s = "abc"
    print(id(s))
    s += "d"       # 生成新 str 对象
    print(id(s))   # id 改变
