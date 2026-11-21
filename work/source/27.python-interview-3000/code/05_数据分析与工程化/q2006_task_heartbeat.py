"""任务心跳:运行中周期上报进度,监控端按心跳年龄识别僵尸任务"""

import json
import os
import tempfile
import time

HEARTBEAT_DIR = tempfile.mkdtemp(prefix="hb_demo_")
STALE_AFTER = 60   # 心跳超过 60 秒未更新视为僵尸


def beat(task, done, total, now):
    path = os.path.join(HEARTBEAT_DIR, task + ".json")
    with open(path, "w") as f:
        json.dump({"done": done, "total": total, "ts": now}, f)


def check(task, now):
    path = os.path.join(HEARTBEAT_DIR, task + ".json")
    if not os.path.exists(path):
        return "无心跳,任务可能没启动", None
    with open(path) as f:
        hb = json.load(f)
    age = now - hb["ts"]
    progress = hb["done"] / hb["total"] if hb["total"] else 1.0
    if age > STALE_AFTER:
        return f"僵尸: 心跳 {age:.0f}s 未更新, 卡在进度 {progress:.0%}", progress
    return f"存活: 进度 {progress:.0%}", progress


if __name__ == "__main__":
    beat("etl_orders", 4200, 10000, now=time.time() - 10)
    beat("etl_users", 9800, 10000, now=time.time() - 600)   # 10 分钟没有心跳
    for t in ("etl_orders", "etl_users"):
        state, _ = check(t, now=time.time())
        print(f"{t}: {state}")
    print("要点:心跳文件写时间戳加进度并原子覆盖;心跳停了但进程还在 = 僵尸,先杀再重放;心跳间隔取任务时长的十分之一,太密伤 IO")
