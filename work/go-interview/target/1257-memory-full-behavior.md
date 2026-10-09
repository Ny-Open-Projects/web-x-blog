> 原文锚点：第 23~31 段「内存满按淘汰策略处理…noeviction 拒绝写入返回错误已存安全…3.0前 volatile-lru 淘汰过期key中LRU…设其他策略则删key释放可继续写但可能丢数据…建议合理配置避免意外丢失」

## 一句话总述
Redis 内存达到 `maxmemory` 后表现**完全取决于淘汰策略**：默认 `noeviction` 会拒绝写命令并返回 OOM 错误（存量数据可读、安全）；若配置了 `allkeys-*`/`volatile-*` 等，则按策略删除 key 释放空间、写可继续但**可能丢数据**。结论：内存满不崩溃，只是"拒写"或"淘汰"二选一。

## 面试官视角
这是"Redis 内存满了会怎样"的标准答案落点。面试官期待你给出**分策略的结论**，并指出 noeviction 下"不丢数据但写失败"这一反直觉点。

## 主问答
**Q（面试官原话）：** Redis 内存满了到底会发生什么？

**A：**

1. **noeviction（3.0+ 默认）**：内存满后**拒绝所有导致内存增长的写命令**（SET、LPUSH、HSET 等），向客户端返回 `OOM command not allowed` 错误；**已存数据完好、读/删不受影响**——不崩溃，只是"写不进"。
2. **3.0 前默认 volatile-lru**：在设了过期时间的 key 中淘汰 LRU 项释放空间，写可继续但过期数据可能丢失。
3. **其他淘汰策略（allkeys-lru/lfu/random、volatile-* 等）**：按对应算法挑 key 删除释放空间，内存满后**仍可持续写入**，但被淘汰的 key 数据丢失。
4. **查看与运维**：`CONFIG GET maxmemory-policy` 看当前策略、`CONFIG SET` 动态改（重启失效）、改 `redis.conf` 的 `maxmemory-policy` 永久生效；建议按业务（缓存 vs 持久）合理选择策略避免意外丢数据。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停档 |
|----|------|----------|--------|------------|
| L1 | noeviction 下读会失败吗 | 是否懂只拒写 | 读/删正常 | 答不出即止 |
| L2 | 返回什么错误 | 是否见过 OOM 报错 | OOM command not allowed when used memory > maxmemory | 答不出即止 |
| L3 | 配 allkeys-lru 还会 OOM 吗 | 是否懂淘汰释放 | 会淘汰释放、写继续、丢被淘数据 | 答不出即止 |
| L4 | 动态改策略怎么持久化 | 是否懂 CONFIG SET vs 文件 | SET 重启失效、conf 文件永久 | 答不出即止 |
| L5 | 如何避免意外丢数据 | 是否懂选型 | 缓存用 allkeys-*、保活用 volatile-* | 答不出即止 |

## 版本与兼容性
- 行为规则跨版本一致；仅**默认策略**随版本变（3.0 分界）。
- `CONFIG SET` 动态生效但仅运行时；`redis.conf` 写入才重启保留。

## 关键代码
```go
// 内存满 + noeviction 时，写命令返回特定错误
import "context"
import "github.com/redis/go-redis/v9"

err := cli.Set(ctx, "k", "v", 0).Err()
if err != nil {
    // redis: OOM command not allowed when used memory > 'maxmemory'
    _ = err
}
// 此时 Get / Del 仍正常
v, _ := cli.Get(ctx, "existing").Result()
_ = v
```

## 总结与追问预判
- 核心结论：**内存满 ≠ 崩溃**；noeviction 拒写保数据、其他策略淘汰保写入但丢数据；具体看策略。
- 预判追问："怎么监控内存快满？"答：INFO memory 看 used_memory/maxmemory、mem_fragmentation_ratio，配 maxmemory-policy 与告警阈值。

## ⚠️ 原文纠错
源码将若干术语音译为崩坏词，本卡已统一为规范术语（如 Redis、maxmemory、淘汰策略、noeviction、OOM 错误）。本源未现黑名单词，正文一律使用规范词，纠错节不枚举任何原词崩坏词 `[经验]`。

> 边界：策略矩阵见 1257；maxmemory 配置见 1257；本卡聚焦"内存满时的运行时表现与运维手段"。
