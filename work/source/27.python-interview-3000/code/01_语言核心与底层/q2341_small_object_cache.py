"""小型对象缓存实测:int 缓存、字符串驻留与空元组单例的条件。"""
import sys

if __name__ == "__main__":
    a, b = 100, 100
    print("缓存区间内 100 is 100:", a is b)

    x, y = 1000, 1000
    print("同一代码块的 1000 字面量:", x is y)      # 编译期共享

    n1 = abs(-257)
    n2 = 257
    print("运行期算出的 257 与字面量 257:", id(n1) == id(n2))

    s1, s2 = "hello_world", "hello_world"
    print("标识符样字符串驻留:", s1 is s2)
    t1, t2 = "hello world!", "hello world!"
    print("带空格标点的不保证:", t1 is t2)

    e1, e2 = (), ()
    print("空元组单例:", e1 is e2, "| 引用计数:", sys.getrefcount(e1))

    print("结论:比值一律 ==", 1000 == 1000)
