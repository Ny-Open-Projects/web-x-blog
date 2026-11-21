import inspect
import sys

def depth():
    f = sys._getframe()
    n = 0
    while f:
        n += 1
        f = f.f_back          # 沿 f_back 链上溯,这就是 Python 栈
    return n

def recurse(n):
    return recurse(n + 1)     # 无限递归,直到撞上递归限制

def traceback_format(e):
    import traceback
    return traceback.format_exception(type(e), e, e.__traceback__)

print("current python stack depth:", depth())
print("recursionlimit:", sys.getrecursionlimit())

try:
    recurse(0)
except RecursionError as e:
    print("RecursionError:", e)

# 回溯本身就是帧链的可读投影
tb_lines = []
try:
    1 / 0
except ZeroDivisionError as e:
    tb_lines = traceback_format(e)

print("".join(tb_lines).splitlines()[-1])

# inspect 能拿到运行期帧
print("callers:", [s.function for s in inspect.stack()][:4])
