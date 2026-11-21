a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True  值相等
print(a is b)  # False 不同对象

x = None
print(x is None)  # True,推荐的判空写法

s1 = "hello"
s2 = "hello"
print(s1 is s2)  # 通常 True,字符串驻留,但这是实现细节

if __name__ == "__main__":
    class Weird:
        def __eq__(self, other):
            return True
    w = Weird()
    print(w == None)   # True,__eq__ 被重载
    print(w is None)   # False
