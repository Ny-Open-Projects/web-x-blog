import dis

def outer():
    x = 10
    def inner():
        return x + 1        # x 是自由变量,经 cell 访问
    return inner

f = outer()
print(f())                 # 11
print(f.__closure__)       # cell 对象元组
print(f.__closure__[0].cell_contents)   # 10,可读也可写(cell_contents 可赋值)

print("---- inner bytecode ----")
dis.dis(f)                 # 看到 LOAD_DEREF 而非 LOAD_FAST/LOAD_GLOBAL

# 经典坑:lambda 捕获变量本身
fs = [lambda: i for i in range(3)]
print([g() for g in fs])   # [2, 2, 2]
fs2 = [lambda i=i: i for i in range(3)]
print([g() for g in fs2])  # [0, 1, 2],默认参数在 def 时固化
