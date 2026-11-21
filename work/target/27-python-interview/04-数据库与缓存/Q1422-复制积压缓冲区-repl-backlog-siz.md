---
title: [Q1422] 复制积压缓冲区: repl-backlog-size 与全量重同步的临界点
date: 2026-11-17
categories: [Python数据库与缓存]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1422 · 复制积压缓冲区: repl-backlog-size 与全量重同步的临界点

> 难度:★★★☆ | 标签:Redis, 复制

**问**:从库断线重连后,什么情况下会触发全量重同步?backlog 怎么算?

**答**:从库重连时带着复制偏移量 offset,若 offset 还落在主库的 repl_backlog 环形缓冲区内,主库只补发增量(部分重同步);offset 已被新写入覆盖(环形缓冲写了一圈)则只能全量重同步——bgsave + 全量传输 + 从库加载,大实例上这是一次昂贵的"重启级"操作,还可能连环打满带宽。backlog 的算账:容量 = 写入速率 × 预期容忍的断线时长,默认 30MB 在 10MB/s 的写入下只兜得住 3 秒断线,高写入实例应按"峰值写入速率 × 60 秒"量级设置。配套要监控 master_repl_offset 与 slave 的差值,差值逼近 backlog 大小就是全量重同步的前兆。记住链条:断线时长 > backlog 秒数 = 全量重同步 = 又一次 fork 阻塞(Q1421)。

```python
# file: code/04_数据库与缓存/q1422_repl_backlog.py
"""复制积压缓冲区: repl-backlog-size 与全量重同步的临界点"""
DEFAULT = 30 * 1024 * 1024

def tolerate_seconds(size_bytes, write_bps):
    return size_bytes / write_bps

print("默认 30MB backlog 的断线容忍时长:")
for mbps in (1, 10, 50):
    print(f"  写入 {mbps} MB/s -> 只兜 {tolerate_seconds(DEFAULT, mbps * 1024 * 1024):.1f} 秒")
need_bps, want_sec = 10 * 1024 * 1024, 60
print(f"写入 {need_bps // 1048576} MB/s 想兜 {want_sec} 秒: backlog 需 {need_bps * want_sec // 1048576} MB")
print("链条: 断线超时 -> 全量重同步 -> bgsave fork -> 又一次延迟毛刺")
```

**追问**:
- 全量重同步期间主库还能写吗?——能,复制不阻塞写;但从库加载 RDB 期间不可用,且主库还要维护重连期间的新增量,资源紧张时是恶性循环。
- PSYNC 怎么判断能不能部分重同步?——从库带 replication id 与 offset 重连,id 匹配且 offset 仍落在 backlog 环形区内就补发增量,否则回退全量。
- backlog 为什么是环形缓冲?——固定内存按写入速率循环覆盖旧数据,只为断线重连窗口服务;容忍时长=大小除以写入速率,这就是算账公式的来源。
- 生产陷阱?——高写入实例沿用默认 30MB,网络抖十秒就升级成全量重同步,连带 fork 阻塞与带宽打满(Q1421);按峰值写入速率乘容忍秒数设置,offset 差值逼近水位先告警。

---
