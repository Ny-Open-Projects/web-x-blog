a = [1, 2, 3]
b = a          # b 与 a 指向同一个 list 对象
b.append(4)
print(a)       # [1, 2, 3, 4] 原地修改影响两个名字

x = 10
y = x
x = 99         # 重新绑定,不影响 y
print(y)       # 10

print(id(a) == id(b))   # True,同一对象
print(a is b)           # True

if __name__ == "__main__":
    demo_a = {"k": 1}
    demo_b = demo_a
    demo_b["k"] = 2
    print(demo_a)  # {'k': 2}
