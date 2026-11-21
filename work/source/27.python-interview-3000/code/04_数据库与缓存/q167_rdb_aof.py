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
