a = [1, 2]
b = a
a += [3]                                  # list 有 __iadd__:原地,b 跟着变
print(a, b, "same object:", a is b)

x = (1, 2)
y = x
x += (3,)                                 # tuple 无 __iadd__:回退 x = x + (3,)
print(x, y, "same object:", x is y)

s1, s2 = "ab", "ab"
id_before = id(s1)
s1 += "c"
print(s1, s2, "rebound:", id(s1) != id_before)

class Basket:
    def __init__(self, items):
        self.items = items

    def __iadd__(self, other):
        self.items.extend(other)          # 原地修改
        return self                       # 必须返回 self

    def __repr__(self):
        return f"Basket({self.items})"

if __name__ == "__main__":
    basket = Basket(["pen"])
    alias = basket
    basket += ["book"]
    print(basket, "alias same:", alias is basket)
