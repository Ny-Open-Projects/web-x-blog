import sys

# 同一 code object 内:相同字面量常量去重(257 也共享)
print(256 is 256)               # True
print(257 is 257)               # 同一 code object 内 True(常量去重,不是常量折叠)
x, y = 257, 257                 # 局部变量仍指向同一常量池对象
print(x is y)                   # True,因为同一函数编译单元

# 字符串:编译期字面量自动 intern,运行期拼接不会
a = "hello_world"
b = "hello_world"
print(a is b)                   # True,字面量 intern
c = "hello" + "_world"
print(c is a)                   # True!常量折叠在编译期完成
d = "".join(["hello", "_world"])
print(d is a, d == a)           # False True,运行期产生不 intern

print(sys.intern("py" + "thon") is sys.intern("python"))  # 手动 intern
