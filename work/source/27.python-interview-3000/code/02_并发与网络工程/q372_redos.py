"""灾难性回溯演示:危险模式 vs 安全模式耗时对比。"""
import re
import time

evil = "a" * 26 + "!"           # 匹配失败,触发全量回溯
danger = re.compile(r"^(a+)+$")  # 嵌套量词,指数回溯
safe = re.compile(r"^a+$")       # 线性匹配的等价写法


def timed(pattern, text):
    start = time.perf_counter()
    try:
        pattern.match(text)
    finally:
        return time.perf_counter() - start


if __name__ == "__main__":
    t1 = timed(danger, evil)
    t2 = timed(safe, evil)
    print(f"danger: {t1:.3f}s  safe: {t2:.6f}s  比例约 {t1 / max(t2, 1e-9):.0f} 倍")
    # 再多几个 a,danger 的耗时成倍增长 —— 指数级
