"""回溯爆炸实测:嵌套量词的耗时曲线与线性改写。"""
import re
import time

EVIL = re.compile(r"(a+)+$")     # 嵌套量词:指数回溯
GOOD = re.compile(r"a+$")        # 线性改写


def timed(match, s):
    t0 = time.perf_counter()
    result = bool(match(s))
    return (time.perf_counter() - t0) * 1000, result


if __name__ == "__main__":
    for n in (18, 20, 22, 24):
        s = "a" * n + "!"
        evil_ms, hit = timed(EVIL.match, s)
        good_ms, _ = timed(GOOD.match, s)
        print(f"len={n:2d}  (a+)+$: {evil_ms:8.1f} ms   a+$: {good_ms:.3f} ms")

    print("结论:每加 2 个字符耗时约翻 4 倍,改写后恒为微秒级")
