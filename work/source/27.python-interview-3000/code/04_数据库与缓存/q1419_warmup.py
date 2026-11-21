"""缓存预热脚本工程化: 幂等、限速与失败重试"""
import time

cache, warmed = {}, set()
fail_once = {"k3": False, "k11": False}    # 模拟这两个 key 第一次回源失败

def load_from_db(k):
    if k in fail_once and not fail_once[k]:
        fail_once[k] = True
        raise IOError("db timeout")
    return f"val-{k}"

def warm(keys, rate=0.001):
    ok = 0
    for k in keys:
        if k in warmed:
            continue                        # 幂等: 已预热直接跳过
        for attempt in range(3):
            try:
                cache[k] = load_from_db(k)
                warmed.add(k)
                ok += 1
                break
            except IOError:
                if attempt == 2:
                    print(f"  key {k} 三次重试失败, 记入失败清单")
        time.sleep(rate)                    # 限速回源, 保护数据库
    return ok

n1 = warm([f"k{i}" for i in range(20)])
n2 = warm([f"k{i}" for i in range(20)])     # 重跑: 全部命中幂等跳过
print(f"首轮预热 {n1} 条, 重跑新增 {n2} 条 <- 幂等让脚本可安全重放")
print("生产要点: 失败清单落盘, 进度断点续传, 回源 QPS 与 DB 承受能力挂钩")
