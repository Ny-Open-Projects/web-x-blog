import random
import time

attempts = {"n": 0}

def flaky_task() -> str:
    attempts["n"] += 1
    if attempts["n"] < 3:
        raise RuntimeError("第三方抖动")
    return "ok"

def autoretry(func, retries: int = 3, base: float = 0.05):
    last = None
    for i in range(retries + 1):
        try:
            return func()
        except Exception as e:
            last = e
            if i < retries:
                time.sleep(base * 2 ** i + random.random() * base)  # 退避+抖动
    raise last

print(autoretry(flaky_task), "尝试次数:", attempts["n"])
