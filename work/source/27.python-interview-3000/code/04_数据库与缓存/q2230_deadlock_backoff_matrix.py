"""死锁与锁等待重试: 按错误分类的退避矩阵"""
import random
import sqlite3
import time

MATRIX = [
    ("database is locked", True, 0.02, 5),
    ("deadlock", True, 0.05, 3),
    ("UNIQUE constraint", False, 0, 0),
    ("no such table", False, 0, 0),
]

def classify(err):
    msg = str(err).lower()
    for kw, retryable, base, maxn in MATRIX:
        if kw.lower() in msg:
            return retryable, base, maxn
    return False, 0, 0

def run_with_retry(fn, log, label):
    attempt = 0
    while True:
        attempt += 1
        try:
            result = fn(attempt)
            log.append("尝试%d 成功" % attempt)
            print("%s: %s" % (label, " | ".join(log)))
            return result
        except Exception as e:
            retryable, base, maxn = classify(e)
            log.append("尝试%d 失败[%s]" % (attempt, str(e)[:22]))
            if not retryable or attempt >= maxn:
                print("%s: %s -> 放弃重试" % (label, " | ".join(log)))
                raise
            delay = base * (2 ** (attempt - 1)) * (0.5 + random.random())
            log.append("退避%0.fms" % (delay * 1000))
            time.sleep(delay)

random.seed(3)
n = {"v": 0}
def flaky(attempt):
    n["v"] += 1
    if n["v"] <= 2:
        raise sqlite3.OperationalError("database is locked")
    return "ok"
run_with_retry(flaky, [], "锁等待路径")

def bad(attempt):
    raise sqlite3.IntegrityError("UNIQUE constraint failed: k")
try:
    run_with_retry(bad, [], "唯一约束路径")
except sqlite3.IntegrityError:
    pass

def dead(attempt):
    raise sqlite3.OperationalError("deadlock found")
try:
    run_with_retry(dead, [], "死锁路径")
except sqlite3.OperationalError:
    pass
print("矩阵决定行为: 瞬时错误退避重试, 确定性错误立即抛出, 重试率异常要回头治锁序")
