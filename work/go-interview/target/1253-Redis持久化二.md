# 1253 Redis 持久化（二）：AOF 与三种刷盘策略

> 分类：Redis | 难度：中 | 题型：原理 | 频率：高 | 关键词：**AOF、追加写命令、fsync、always、everysec、no**

> 原文锚点：第 31~62 段「AOF 追加命令、写缓冲/内核缓冲/fsync、三刷盘策略 always/everysec/no」

## 一句话总述
AOF 以「追加写命令」方式持久化：Redis 把每个写命令（如 set/del）追加到 AOF 文件末尾（仅记录写操作，不记读）。写入先进 aof_buf，再 write 到内核缓冲区，最后由 fsync 落盘。落盘策略有三种：always（每条都 fsync，最安全最慢）、everysec（每秒一次，默认）、no（交给 OS，最快最易丢）。

## 面试官视角
AOF 题考「数据安全 vs 性能」的权衡。考官期待你讲清写盘链路（aof_buf → write → 内核缓冲 → fsync → 磁盘）与三策略的可靠性/性能排序：可靠性 always > everysec > no，性能相反。能点出「everysec 最多丢 1 秒、always 增主线程 CPU」是加分点。

## 主问答
**Q（面试官原话）：** AOF 是什么？三种刷盘策略有什么区别？

1. **AOF 本质**：只记录写命令的文本日志，恢复时重放命令重建数据；与 RDB 存「数据」不同，AOF 存「操作」。
2. **写盘链路**：命令执行完先写 `aof_buf` → 调用 write 进内核缓冲区（此时未真正落盘）→ fsync 强制刷到磁盘才返回。
3. **always**：每条写命令后都 fsync，数据最安全，但主线程频繁等落盘、CPU/IO 开销大。
4. **everysec（默认）**：每秒 fsync 一次，最多丢 1 秒数据，性能与安全折中。
5. **no**：不主动 fsync，由操作系统调度回写，性能最好但丢数据量不可控。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | AOF 记录什么？ | 说不清写命令 |
| L2 | 写盘链路？ | 说不清 buf/write/fsync |
| L3 | 三策略？ | 说不全 |
| L4 | 可靠性排序？ | 排反 |
| L5 | everysec 丢多少？ | 说不清最多 1 秒 |

## 版本与兼容性
| 策略 | 可靠性 | 性能 |
|------|--------|------|
| always | 最高 | 最低 |
| everysec | 中 | 中（默认） |
| no | 最低 | 最高 |

## 关键代码
```bash
appendonly yes          # 开启 AOF
appendfsync everysec    # 刷盘策略
```

## 总结与追问预判
核心：**AOF 存写命令、aof_buf→write→fsync 链路、三策略 always/everysec/no 在安全与性能间取舍**。追问常接「AOF 文件过大怎么办」（见 1253）。

## ⚠️ 原文纠错
1. 事实核校： [经验] AOF 追加写命令(只记写不记读)、aof_buf→write→fsync 链路、三策略语义与默认 everysec、可靠性/性能排序——均正确，本卡为准。
2. 崩坏词归一：源码将 Redis/AOF/fsync/写时复制/Memcached 等音译为多组崩坏词；本卡统一为规范术语。
