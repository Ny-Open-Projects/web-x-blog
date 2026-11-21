import sys
import tracemalloc

def deep(n, holder):
    big = bytearray(1024 * 1024)          # 每层 1MB 局部变量
    if n == 0:
        raise ValueError("deep boom")
    return deep(n - 1, holder)

kept = []

def leaky():
    try:
        deep(3, kept)
    except ValueError as e:
        kept.append(e)                    # 连同整条 tb 链一起保留

def fixed():
    import traceback
    try:
        deep(3, kept)
    except ValueError as e:
        kept.append("".join(traceback.format_exception_only(type(e), e)))  # 只留字符串

tracemalloc.start()
for _ in range(20): leaky()
print("leaky kept MB:", round(tracemalloc.get_traced_memory()[0] / 2**20, 1))
kept.clear()
tracemalloc.reset_peak()
for _ in range(20): fixed()
print("fixed kept MB:", round(tracemalloc.get_traced_memory()[0] / 2**20, 1))
print("except 块结束后 e 已被解释器隐式删除:", "e" not in dir())
