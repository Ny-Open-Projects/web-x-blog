# 136 translog 崩溃恢复与可靠性窗口

> 分类：Elasticsearch · 持久化 | 难度：L3 | 题型：可靠性题 | 频率：中 | 关键词：**translog**/**宕机恢复**/**异步写丢数据**/**MySQL binlog 类比**/**OS cache**
> 原文锚点：第 51~58 段「translog 记录 buffer/OS cache 中操作；宕机重启从 translog 恢复；异步写 translog 可丢 n 秒数据；机制类似 MySQL binlog」

## 一句话总述
写入时文档先留在**内存 buffer**和 **OS cache**（都易失），故 ES 把操作额外写入 **translog** 日志；节点宕机重启时自动读 translog 把 buffer/OS cache 中的数据恢复回来——机制类似 MySQL binlog。在容忍少量丢失的场景（日志、可重放数据）可把 translog 设**异步写**换吞吐，但崩溃会丢最后 n 秒（buffer+translog 的 OS cache + segment 的 OS cache 都未落盘）的数据。

## 面试官视角
- 考察意图：是否理解 translog 的"崩溃恢复"本职与"异步写"的可靠性代价，而非只把它当调优旋钮。
- 分档：P5 知 translog 防丢；P6 知宕机从 translog 恢复；P7 能讲清"异步写 translog 丢 n 秒"的丢失窗口与适用场景。
- 红旗：以为 translog 永远同步、零丢失；或不知道异步写会丢数据。
- 惊艳点：点出"丢失窗口 = buffer + translog 的 OS cache + 新 segment 的 OS cache 都未 fsync 的部分"，且类比 MySQL binlog 帮助面试官秒懂。

## 主问答
**Q（面试官原话）：** translog 到底有什么用？设成异步会有什么后果？
**A：**
1. **崩溃恢复本职**：数据写入先驻留内存 buffer 与 OS cache，节点宕机即丢。translog 把每次操作记到磁盘日志，重启时 ES 读 translog 把内存中未落盘的数据恢复回来——与 MySQL binlog 思路一致 `[经验]`。
2. **异步写吞吐换可靠**：默认 translog 每次写都 fsync（durability=request）；设 `async` 后按间隔批量 fsync，吞吐上升。但崩溃时**最后 n 秒**（buffer、translog 的 OS cache、新 segment 的 OS cache 都还在内存）会丢失。
3. **适用场景**：仅日志、或业务能重放指定用户数据的场景，才值得用异步换性能；核心业务别碰。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | translog 干嘛？ | 基础 | 崩溃恢复 | P5 |
| L2 | 重启怎么恢复？ | 机制 | 读 translog 重建 buffer/cache | P6 |
| L3 | 异步写后果？ | 代价 | 丢最后 n 秒 | P7 |
| L4 | 类似啥？ | 类比 | MySQL binlog | P7 |
| L5 | 何时用异步？ | 场景 | 日志/可重放 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 2.x+ | translog durability 参数（request/async） | 答"translog 用于宕机恢复（类比 binlog）；async 换吞吐但丢 n 秒，仅日志类场景用" |

## 关键代码
```go
// 日志场景：用异步 translog 换吞吐，容忍少量丢失
// 通过 Go ES 客户端设置索引级 translog 参数
_, err := cli.IndexPutSettings("logs").
    BodyString(`{"index.translog.durability":"async","index.translog.sync_interval":"10s"}`).
    Do(ctx)
if err != nil {
    log.Fatal(err)
}
// 核心业务保持默认 request（每次写都 fsync，零丢失窗口）
```

## 总结与追问预判
translog 是 ES 的"binlog"——崩溃恢复的基石；异步写是明确的可靠性换性能取舍。调优角度见 1316-refresh-translog；写入全流程见 136-write-lifecycle.deep。

## ⚠️ 原文纠错
1. 事实核校：translog 记录内存中操作、宕机从 translog 恢复、异步写丢 n 秒、类比 MySQL binlog、仅日志/可重放场景用异步——均正确 `[经验]`。
2. 崩坏词归一：源码将 Elasticsearch 音译为崩坏词、translog 音译为 transforer/translog 的崩坏、OS cache 音译为 OS 开启/OSK、binlog 音译为 billog、宕机音译为当机；源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
