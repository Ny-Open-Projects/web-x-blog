---
title: [A125] WAL 与检查点：崩溃恢复的一致性
date: 2026-11-20
categories: [Python算法笔试]
tags: [Python面试, 笔试题, 27]
type: 笔试题
---

### A125 · WAL 与检查点

> 难度:★★★ | 标签:WAL, 崩溃恢复, 可靠性

**问**（笔试·编程+场景题）：实现一个带 WAL 的键值存储——「写内存成功但进程崩溃数据丢失」怎么救（WAL 写序：先日志后内存），WAL 的 fsync 时机怎么选（每次/批量——丢数据窗口与吞吐的权衡），检查点（checkpoint）怎么把 WAL 截短，恢复时「WAL 末尾半条记录」怎么处理（torn write）？

**答**：① WAL 铁律：**先写日志（含 fsync）再改内存**——崩溃后重放 WAL 恢复到崩溃前最后一条完整事务；顺序：日志 append → fsync → 内存应用 → 确认客户端。② fsync 策略：**每写必刷**（durability 强，吞吐被磁盘限）vs **组提交**（攒 N ms 批量刷——丢数据窗口 = 组间隔，吞吐高数倍）——选型按业务：金融每写刷，日志类组提交。③ 检查点：把当前内存状态整体落盘（快照文件），之后的 WAL 只需保留检查点之后的增量——**截短 WAL** 防无限增长；检查点时机：定期或 WAL 超过阈值；做检查点期间的写入怎么办——检查点基于「生成时状态」+ 新写入继续进 WAL（恢复 = 快照 + 快照后 WAL 重放）。④ Torn write：磁盘写是以扇区为单位的，崩溃可能留下半条记录——**每条记录带长度+CRC**，恢复时从头重放，遇到 CRC 不合法/长度不足即停止（丢弃尾部）——WAL 保证的是「完整条目不丢」，不保证崩溃瞬间正在写的条目存活。

```python
# 全部标准库；demo 实现带 CRC 的 WAL + 检查点 + torn-write 安全恢复
import json, hashlib, os, tempfile

class KV:
    def __init__(self, path: str, group_ms: float = 0):
        self.path, self.mem = path, {}
        self.wal = open(path, "ab")            # append-only
        self.group_ms = group_ms
        self.pending = []                      # 组提交缓冲
        self._recover()
    @staticmethod
    def _encode(entry: dict) -> bytes:
        body = json.dumps(entry, sort_keys=True).encode()
        crc = hashlib.sha256(body).hexdigest()[:8]
        return len(body).to_bytes(4, "big") + crc.encode() + body   # len + crc + body
    def put(self, k: str, v, sync: bool = True):
        entry = {"op": "put", "k": k, "v": v}
        self.pending.append(entry)
        self.wal.write(self._encode(entry))
        if sync:                               # 每写必刷（强持久化）
            self.flush()
        else:
            self.mem[k] = v                    # 组提交：先应用后异步刷（丢窗口=组间隔）
    def flush(self):
        for e in self.pending:
            self.mem[e["k"]] = e["v"]
        self.pending.clear()
        self.wal.flush()
        os.fsync(self.wal.fileno())            # 真实 fsync（demo 文件同语义）
    def _recover(self):
        """重放 WAL：CRC 校验失败/长度不足即停（torn write 尾部丢弃）。"""
        if not os.path.exists(self.path):
            return
        with open(self.path, "rb") as f:
            while True:
                head = f.read(4)
                if len(head) < 4:
                    break                       # 尾部不完整：丢弃
                n = int.from_bytes(head, "big")
                body = f.read(n)
                if len(body) < n or hashlib.sha256(body[8:]).hexdigest()[:8] != body[:8].decode():
                    break                       # CRC 不符：torn write，安全停止
                self.mem[json.loads(body[8:])["k"]] = json.loads(body[8:])["v"]
    def checkpoint(self):
        """检查点：状态整体落盘 + 截短 WAL（新 WAL 只含之后的增量）。"""
        snap_path = self.path + ".snap"
        with open(snap_path, "w") as f:
            json.dump(self.mem, f)
        self.wal.close()
        open(self.path, "wb").close()          # 截短（demo 简化：清空；生产截到 checkpoint LSN）
        self.wal = open(self.path, "ab")
        return f"checkpoint @ {len(self.mem)} keys"

if __name__ == "__main__":
    path = tempfile.mktemp(suffix=".wal")
    kv = KV(path)
    kv.put("a", 1); kv.put("b", 2)
    assert kv.mem == {"a": 1, "b": 2}
    print("写入并 fsync:", kv.mem)
    kv2 = KV(path)                              # 模拟崩溃后重启：从 WAL 恢复
    assert kv2.mem == {"a": 1, "b": 2}
    print("崩溃恢复（WAL 重放）✅:", kv2.mem)
    kv2.put("c", 3, sync=False)                 # 组提交模式
    print("checkpoint:", kv2.checkpoint())
    # 模拟 torn write：往 WAL 追加半条记录，重启应安全丢弃
    with open(path, "ab") as f:
        f.write(b"\x00\x00\x00\x10partial-writ")   # 长度声称 16 但内容只有 12 且无 CRC
    kv3 = KV(path)
    assert kv3.mem == {"a": 1, "b": 2, "c": 3}     # 半条被丢弃，完整数据完好
    print("torn write 尾部丢弃 ✅（WAL 保证完整条目不丢）")
```

**追问**：1) 组提交的丢数据窗口和「WAL 本来就是防丢」矛盾吗？——不矛盾：组提交丢的是「尚未 fsync 的尾部」，窗口内崩溃这些条目丢失——选型是业务权衡（金融每写刷、日志类组提交）；「已确认给客户端的写」绝不能在组内丢（确认时机必须在 fsync 之后——写序纪律）。2) 检查点和 WAL 截短的原子性？——先写快照（含 fsync）→ 再截 WAL；顺序反了崩溃后「WAL 没了快照没写成」= 数据全丢；生产实现用「新 WAL 文件原子改名」替代截短。3) 为什么不用 SQLite 而自己造？——学习口径（面试考原理）；生产直接用 SQLite/RocksDB（十年打磨的边界情况），自研存储是最大最贵的坑。

## 背诵要点
1. WAL 铁律：先日志（含 fsync）后内存再确认——崩溃重放恢复到最后完整事务。
2. fsync 选型：每写刷（强持久化低吞吐）vs 组提交（丢窗口=组间隔，高吞吐）；确认给客户端必须在 fsync 之后。
3. Torn write：len+CRC 每条记录，恢复遇非法即停（尾部丢弃）——WAL 保证完整条目不丢；检查点先快照后截 WAL。

## 复盘追问
1. 检查点做到一半崩溃，快照文件半截怎么办？（提示：快照写临时文件 + 原子 rename（同 Q7014 镜像口径）——半截快照永不进入恢复路径）
2. WAL 文件本身损坏（扇区坏）怎么办？（提示：损坏点之后的全部丢失——靠双写/镜像 WAL 或备份链兜底；这是「WAL 不是备份」的口径，备份归备份）
