"""断点续跑:分片清单 + 检查点原子写,tmp 加 rename 防止半写状态"""

import json
import os
import tempfile

SHARDS = ["shard_00", "shard_01", "shard_02", "shard_03"]
CHECKPOINT = os.path.join(tempfile.gettempdir(), "q1454_checkpoint.json")


def load_checkpoint(path):
    if not os.path.exists(path):
        return {"done": []}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_checkpoint(state, path):
    """先写临时文件再原子 rename,进程崩溃也不会留下半写的检查点"""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def run_pipeline(shards, crash_after=2):
    state = load_checkpoint(CHECKPOINT)
    print("恢复自检查点,已完成:", state["done"])
    processed = 0
    for shard in shards:
        if shard in state["done"]:
            print(f"  跳过 {shard}")
            continue
        print(f"  处理 {shard}")
        processed += 1
        state["done"].append(shard)
        save_checkpoint(state, CHECKPOINT)  # 每片完成即落盘
        if processed >= crash_after:
            print(f"  (模拟在处理 {shard} 后进程被杀)")
            break
    return state


if __name__ == "__main__":
    if os.path.exists(CHECKPOINT):
        os.remove(CHECKPOINT)
    print("第一次运行:")
    run_pipeline(SHARDS, crash_after=2)
    print("第二次运行:")
    run_pipeline(SHARDS, crash_after=99)
    print("最终检查点:", load_checkpoint(CHECKPOINT))
    os.remove(CHECKPOINT)
