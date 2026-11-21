import json
import os
import tempfile

CHECKPOINT = os.path.join(tempfile.gettempdir(), "q1071_ckpt.json")

def load_done():
    if os.path.exists(CHECKPOINT):
        with open(CHECKPOINT, encoding="utf-8") as f:
            return set(json.load(f))
    return set()

def save_done(done):
    tmp = CHECKPOINT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(sorted(done), f)
    os.replace(tmp, CHECKPOINT)  # 原子替换,崩溃不会留下半写状态

def run(shards):
    done = load_done()
    for s in shards:
        if s in done:
            print("跳过已完成分片", s)
            continue
        print("处理分片", s)
        done.add(s)
        save_done(done)

if __name__ == "__main__":
    run([f"shard-{i}" for i in range(4)])
    print("第二次执行(模拟重跑):")
    run([f"shard-{i}" for i in range(4)])
    os.remove(CHECKPOINT)
