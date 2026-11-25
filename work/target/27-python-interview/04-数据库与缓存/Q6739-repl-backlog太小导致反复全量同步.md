---
title: "[Q6739] 抖一下就全量同步：repl-backlog 太小与 fork 抖动"
date: 2026-11-24
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6739 · 抖一下就全量同步：repl-backlog 太小与 fork 抖动

难度：P7 ｜ 标签：Redis、复制、repl-backlog、全量同步、fork/COW

基线：Python 3.12；Redis 7 `repl-backlog-size`、`repl-diskless-sync`、`sync_full/sync_partial_*` 计数器。

**问**：主从之间网络偶发 3 秒抖动，每次抖动后 `master_link_status` 短暂 down 又恢复，但主库 CPU 尖刺、`latest_fork_usec` 飙到 800ms、内存 RSS 明显上涨，从库日志是 `Full resync from master`。断线才 3 秒，为什么不能增量续传？

**答**：
- **结论**：重连时副本发 `PSYNC <replid> <offset>` 请求**部分重同步**，主库只有在 `repl-backlog`（环形缓冲区）里还能找到这个 offset 时才回 `+CONTINUE`；找不到就回 `+FULLRESYNC`，走全量：fork 子进程写 RDB（COW 期间写放大 → RSS 上涨）、传输、从库清空加载。`repl-backlog-size` 默认只有 1MB，高写入量下几秒就能写满 → 必然退化为全量。
- **取舍**：backlog 是纯内存（每个副本一份，默认 1MB），调大到 64~256MB 能覆盖分钟级断线，代价是内存；`repl-diskless-sync` 省磁盘 IO，但要等 `repl-diskless-sync-delay`（默认 5s）聚合多个副本的请求；fork 抖动取决于实例内存、页表大小和 THP（透明大页开着时 COW 单位从 4KB 变 2MB，复制一字节也要拷整页）。
- **实战**：① 按"写入速率 × 可容忍断线秒数"算 backlog，再留 2 倍余量；② 关闭 THP（`/sys/kernel/mm/transparent_hugepage/enabled` 设 `never`）；③ 监控 `sync_full`、`sync_partial_ok`、`sync_partial_err` 三个计数器，`sync_partial_err` 增长就是 backlog 不够；④ 大批量导入避开高峰，必要时先摘副本；⑤ 主库内存预留出 fork 期间的 COW 峰值。

```python
"""repl-backlog 环形缓冲：能不能部分重同步取决于 offset 是否还在窗口内。"""


class Backlog:
    def __init__(self, size_bytes: int) -> None:
        self.size = size_bytes
        self.chunks: list[tuple[int, int]] = []   # (offset_end, nbytes)
        self.total = 0
        self.start_offset = 0
        self.end_offset = 0
        self.full_resync = 0
        self.partial_ok = 0
        self.partial_err = 0

    def append(self, nbytes: int) -> None:
        self.chunks.append((self.end_offset, nbytes))
        self.total += nbytes
        while self.total > self.size and self.chunks:
            _, old = self.chunks.pop(0)
            self.total -= old
            self.start_offset = self.chunks[0][0] if self.chunks else self.end_offset
        self.end_offset += nbytes

    def psync(self, repl_offset: int) -> str:
        if self.start_offset <= repl_offset <= self.end_offset:
            self.partial_ok += 1
            return "CONTINUE"
        self.partial_err += 1
        self.full_resync += 1
        return "FULLRESYNC"


def simulate(backlog_size: int, write_rate_mb_s: float, outage_s: int,
             pre_s: int = 10) -> None:
    bl = Backlog(backlog_size * 1024 * 1024)
    step = 64 * 1024
    per_s = write_rate_mb_s * 1024 * 1024 / step

    for _ in range(int(per_s * pre_s)):        # 断线前：正常写入
        bl.append(step)
    break_offset = bl.end_offset               # 副本最后确认的位点

    for _ in range(int(per_s * outage_s)):     # 断线期间：主库继续写
        bl.append(step)

    result = bl.psync(break_offset)
    lag_mb = (bl.end_offset - break_offset) / 1024 / 1024
    print(f"backlog={backlog_size:>4}MB 写={write_rate_mb_s}MB/s 断线={outage_s}s"
          f" 落后={lag_mb:.0f}MB -> {result}")


if __name__ == "__main__":
    # 20MB/s 写 3 秒 = 60MB，1MB 的 backlog 早把断线位点挤掉了
    simulate(1, 20, 3)
    # 调到 128MB 就能覆盖
    simulate(128, 20, 3)
    # 断线 30 秒 = 600MB，128MB 也不够
    simulate(128, 20, 30)

    print("结论：backlog 要按 写入速率 × 断线容忍 来算，默认 1MB 在高写入下形同虚设")
```

**追问一**：`sync_partial_err` 增长说明什么？
→ 解析：副本带了 offset 来请求 `PSYNC`，但主库无法满足（offset 早于 backlog 起点，或 `replid` 不匹配，比如发生过主从切换）。这就是"想增量却被拒"，通常意味着 backlog 太小或断线太久。持续增长要立刻调大 backlog。

**追问二**：全量同步时 fork 耗时由什么决定？
→ 解析：页表规模（实例内存 / 页大小）、THP 是否开启、`vm.overcommit_memory=1` 是否配置。内存越大页表越深，fork 复制页表越慢；THP 开启时 COW 以 2MB 为单位，写一个字节也要复制整页，既放大延迟也放大内存峰值。
