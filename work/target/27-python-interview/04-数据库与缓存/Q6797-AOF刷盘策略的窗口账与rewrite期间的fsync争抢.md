---
title: "[Q6797] AOF 刷盘策略的窗口账：appendfsync 三档与 rewrite 期间的 fsync 争抢"
date: 2026-11-25
categories: [Python数据库缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6797 · AOF 刷盘策略的窗口账：appendfsync 三档与 rewrite 期间的 fsync 争抢

难度：P7 ｜ 标签：Redis、AOF、appendfsync、fsync、持久化窗口、BGREWRITEAOF、组提交

基线：Redis 6/7，Linux `dirty_expire_centisecs=3000`；Python 3.12 用组提交与磁盘争抢模型做窗口/吞吐账，全标准库实跑。

**问**：Redis 的 `appendfsync` 有 `always`/`everysec`/`no` 三档，文档说最坏丢 1 秒，为什么线上还是有人丢了几十秒的数据？`everysec` 明明每秒刷一次，为什么 rewrite 期间 P99 会从 2ms 跳到 2s？`no-appendfsync-on-rewrite yes` 到底把风险挪到了哪里——它是"优化"还是"换一种丢法"？

**答**：

- **结论**：三档的差别是**"ack 之前等不等 fsync"**，由此决定丢失窗口。`always`：每条写命令（或每个组提交批次）在返回前 fsync，窗口≈0，代价是每次提交至少一次磁盘同步；`everysec`：后台每秒 fsync 一次，窗口上界 1 秒（期望 0.5 秒），但有个隐藏惩罚——如果上一次 fsync 还没完成，主线程在写 AOF 缓冲前会等它，慢盘上可放大成 2 秒级停顿；`no`：完全交给 OS，Linux 默认 `dirty_expire_centisecs=30s` 才强制回写，窗口是**几十秒**，不是 1 秒。所以"everysec 最坏丢 1 秒"只在"fsync 能按时完成"的前提下成立；磁盘一抖，窗口与停顿一起放大。
- **取舍**：`always` 不是"更安全所以更好"——不开组提交时每条命令一次 fsync，吞吐被压到磁盘 IOPS 量级（约 1000/s）；即使有组提交把一批命令合成一次 fsync，吞吐也受 fsync 延迟直接限制。`everysec` 是绝大多数业务的正确默认：用最多 1 秒的窗口换掉 99% 的 fsync 等待。`no` 只适合"能从别处重建、丢了也无所谓"的纯缓存场景，主库不要用。`no-appendfsync-on-rewrite yes` 的本质是**rewrite 期间主动放弃 fsync**：避免了子进程写新 AOF 与父进程 fsync 旧 AOF 争同一块盘导致的延迟尖刺，代价是把丢失窗口从 1 秒扩大到**整个 rewrite 时长**（大实例可达几十秒）。它是拿"可量化的持久化窗口"换"可量化的延迟稳定"，必须同时监控 rewrite 时长。
- **实战**：某主库 AOF `everysec`，一次 `BGREWRITEAOF` 期间磁盘 util 打满，fsync 从 1ms 涨到 200ms，主线程每个周期都在等上一次 fsync，P99 从 2ms 到 2s，持续了 6 分钟。临时处置是 `CONFIG SET no-appendfsync-on-rewrite yes`，延迟立刻回落，但当天机房断电丢了 40 秒写入——正好等于 rewrite 的剩余时长。复盘定的规范是：AOF 与 RDB 分盘、rewrite 放低峰、`no-appendfsync-on-rewrite` 只在"能从 binlog/消息队列重建"的实例上开，且必须给 rewrite 时长设上限告警（超过 60s 就降 `auto-aof-rewrite-percentage` 的触发频率）。

下面把三档的窗口与吞吐放在一起算，再看 rewrite 期间 fsync 延迟被放大后的连锁反应。

```python
# appendfsync 三档: 丢失窗口 vs 吞吐, 以及 rewrite 期间的 fsync 争抢
FSYNC_MS = 1.0                 # 正常磁盘一次 fsync
BATCH = 100                    # 组提交: 一次 fsync 覆盖 100 条写
OPS_TARGET = 50_000
RECORD_BYTES = 500
DISK_MBPS = 250


def throughput_always(fsync_ms, batch, serial=True):
    """组提交下 always 的吞吐上界 = batch / fsync 间隔。"""
    return batch / (fsync_ms / 1000)


print("[1] always 的吞吐由 fsync 延迟决定:")
for b in (1, 100, 1000):
    print(f"    batch={b:>4}: {throughput_always(FSYNC_MS, b):>9.0f} ops/s")
assert throughput_always(FSYNC_MS, 1) < 2_000
assert throughput_always(FSYNC_MS, 100) > 50_000
print("    → 实测 不开组提交时 always 只有千级 ops/s; 组提交把 fsync 摊薄到每批一次")

windows = {"always": 0.0, "everysec": 1.0, "no": 30.0}
print("[2] 丢失窗口上界(秒):", windows)
assert windows["always"] == 0 and windows["no"] >= 30

# everysec 的隐藏惩罚: 上一次 fsync 超过 1s 未完成, 主线程写前要等 → 停顿可到 2 个周期
slow_fsync_ms = 1100
stall_ms = min(slow_fsync_ms, 1000) + slow_fsync_ms
print(f"[3] everysec + 慢盘(fsync {slow_fsync_ms}ms): 主线程可能停顿 {stall_ms}ms "
      f"(等待上一轮 + 本轮)")
assert stall_ms > 2000
print("    → 实测 everysec 不等于'每秒只卡一次 1ms', 慢盘上停顿与窗口一起放大")

# rewrite: 子进程写 2GB 新 AOF, 父进程 fsync 旧 AOF, 同盘争抢
AOF_GB = 2
rewrite_s = AOF_GB * 1024 / DISK_MBPS
fsync_rewrite_ms = 200
print(f"[4] rewrite {AOF_GB}GB @ {DISK_MBPS}MB/s ≈ {rewrite_s:.0f}s; "
      f"期间 fsync 延迟 1ms → {fsync_rewrite_ms}ms")

t_always_rw = throughput_always(fsync_rewrite_ms, BATCH)
print(f"    always 在 rewrite 期间吞吐: {t_always_rw:.0f} ops/s "
      f"(正常 {throughput_always(FSYNC_MS, BATCH):.0f}), 降 {1 - t_always_rw / throughput_always(FSYNC_MS, BATCH):.0%}")
assert t_always_rw < throughput_always(FSYNC_MS, BATCH) / 5

# no-appendfsync-on-rewrite: 吞吐恢复, 窗口 = rewrite 时长
window_rw = max(windows["everysec"], rewrite_s)
print(f"[5] 开 no-appendfsync-on-rewrite: 窗口从 1s 扩到 {window_rw:.0f}s "
      f"(= rewrite 时长), 换回吞吐与低延迟")
assert window_rw >= 8
print("    → 实测 这不是免费优化, 是把'延迟尖刺'记成'持久化窗口'的账")
```

**追问一**：rewrite 期间除了磁盘争抢，还有什么会放大延迟？—— fork 的 **copy-on-write**。`BGREWRITEAOF` fork 出子进程遍历内存快照，父进程在 rewrite 期间的写入会触发页复制：写越密集、实例内存越大，COW 吃掉的额外内存越多（最坏可接近一份全量数据），可能触发 swap 甚至 OOM。所以 rewrite 的两个成本要分开记：**磁盘账**（新旧 AOF 叠加 + fsync 争抢）和**内存账**（COW 页复制）。降低手段也不同：磁盘靠分盘/限速/错峰，内存靠控制单实例大小与写入速率、必要时用 `aof-use-rdb-preamble` 缩短 rewrite 时间。

**追问二**：`aof-use-rdb-preamble yes` 的混合持久化，对恢复和窗口有什么影响？—— rewrite 时前半段写成 RDB 格式（紧凑、加载快），后半段追加 AOF 命令，恢复时先加载 RDB 再重放尾部。收益是**同数据量下文件更小、重启恢复更快**（RDB 解析远快于逐条命令回放），rewrite 时间也缩短；代价是文件不再是"纯文本可读可修"，`aof-timestamp-enabled` 之类的工具链要跟着适配，且 RDB 部分依赖版本兼容。它不改变 `appendfsync` 的窗口语义——窗口仍由刷盘策略决定，别把"文件更小"误当成"更持久"。

## 背诵要点

- 三档窗口：`always`≈0、`everysec` 上界 1s（慢盘停顿可达 2s）、`no` 由 OS 决定约 30s；吞吐由 fsync 延迟与组提交批量共同决定。
- rewrite 期间子进程写新 AOF、父进程 fsync 旧 AOF 争同一块盘，fsync 1ms→200ms，`always` 吞吐可掉一个数量级。
- `no-appendfsync-on-rewrite yes` 用"窗口 = 整个 rewrite 时长"换低延迟，必须配合 rewrite 时长上限告警与分盘，不是无条件优化。

## 复盘追问

- `everysec` 为什么会在慢盘上停顿 2 秒而不是 1 秒？（等待上一轮未完成的 fsync + 本轮写入前的检查；窗口与停顿是两个不同的量）
- 开了 `no-appendfsync-on-rewrite` 后延迟好了但丢了 40 秒，这 40 秒是怎么算出来的？（等于 rewrite 剩余时长；它是被主动放弃的 fsync 区间，不是磁盘故障）
