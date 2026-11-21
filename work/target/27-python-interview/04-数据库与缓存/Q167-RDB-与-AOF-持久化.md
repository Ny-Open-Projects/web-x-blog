---
title: [Q167] RDB 与 AOF 持久化
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q167 · RDB 与 AOF 持久化

> 难度:★★★ | 标签:Redis, 持久化

**问**:Redis 的 RDB 和 AOF 有什么区别?如何选择?

**答**:RDB 是某时刻全量快照,二进制紧凑、恢复快,但 save 点之间宕机会丢数据;AOF 记录每条写命令,appendfsync everysec 时最多丢 1 秒,文件大恢复慢,靠 AOF rewrite 压缩。生产常用混合持久化(4.0+ aof-use-rdb-preamble):重写时先写 RDB 全量再追加增量 AOF,兼得恢复速度与低丢失。纯缓存场景也可只靠主从复制不持久化。

```python
# file: code/04_数据库与缓存/q167_rdb_aof.py
"""用文件模拟 RDB 快照与 AOF 追加日志的恢复过程"""
import json
import os

SNAP, LOG = "/tmp/q167_snap.json", "/tmp/q167.aof"


def rdb_snapshot(state: dict) -> None:
    with open(SNAP, "w", encoding="utf-8") as f:     # 全量覆盖写, 类似 SAVE
        json.dump(state, f)


def aof_append(command: str, *args) -> None:
    with open(LOG, "a", encoding="utf-8") as f:      # 只追加写命令
        f.write(json.dumps([command, *args]) + "\n")


def load() -> dict:
    state = {}
    if os.path.exists(SNAP):                          # 先载入快照
        with open(SNAP, encoding="utf-8") as f:
            state = json.load(f)
    if os.path.exists(LOG):                           # 再重放 AOF 增量
        with open(LOG, encoding="utf-8") as f:
            for line in f:
                cmd, *args = json.loads(line)
                if cmd == "SET":
                    state[args[0]] = args[1]
                elif cmd == "DEL":
                    state.pop(args[0], None)
    return state


if __name__ == "__main__":
    rdb_snapshot({"k1": "v1"})
    aof_append("SET", "k2", "v2")
    aof_append("SET", "k1", "v1_new")
    aof_append("DEL", "k1")
    print("恢复结果:", load())     # {'k2': 'v2'} 快照 + 日志重放
```

**追问**:
- AOF 的三种 fsync 策略?——always 最安全最慢、everysec 折衡(推荐)、no 交给 OS 最快但可能丢较多。
- AOF rewrite 做什么?——根据当前内存数据生成等价最小命令集替换旧 AOF,期间新写命令写入缓冲区续上。

---
