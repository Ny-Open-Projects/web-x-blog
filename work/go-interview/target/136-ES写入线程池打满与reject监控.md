# 136 ES 写入线程池打满与 reject 监控

> 分类：Elasticsearch · 写入运维 | 难度：L3 | 题型：调优题 | 频率：中 | 关键词：**write 线程池**/**reject**/**429 重试**/**bulk 调参**/**cat threadpool**
> 原文锚点：第 19~28 段「写线程池打满 reject 写请求；429 重试；bulk 调大小/数量/间隔；cat threadpool 看 reject/queue/active」

## 一句话总述
ES 每个数据节点有专用于处理 get/search/write 的**线程池**；写入线程池打满时会**拒绝（reject）写请求，可能丢数据**——业务层须按返回状态码（429）重试，并调 bulk 的批次大小/文档数/间隔避免被拒；用 `cat threadpool` 看 `reject`/`queue`/`active` 三列监控拥堵。

## 面试官视角
- 考察意图：是否知道"ES 不是无脑接写入"，有线程池队列上限与拒绝语义，以及生产如何兜底。
- 分档：P5 知写会被 reject；P6 知 429 重试 + bulk 调参；P7 知 `cat threadpool` 三列含义与"queue 持续高=拥堵"判据。
- 红旗：以为写失败就静默丢；或 bulk 越大吞吐越高（实则易触发 reject）。
- 惊艳点：点出"reject 列 > 0 即有过拒绝、queue 列高即拥堵、active 列=正在处理的线程数"——把监控三列讲透。

## 主问答
**Q（面试官原话）：** 写入大量数据，ES 开始拒写了，怎么办？
**A：**
1. **reject 语义**：数据节点的 write 线程池满后**拒绝新写请求**，被拒的写会丢——业务层必须**按写入返回状态码判断**，出现 `429` 就**重试**（带退避）`[经验]`。
2. **bulk 调参**：用 bulk 时调**批次大小 / 文档数量 / 提交间隔**，别一次塞太大；过大反而更易触发 reject，吞吐不升反降。
3. **监控**：`GET _cat/threadpool` 看三列——`reject`（被拒次数，>0 即有拒绝）、`queue`（当前排队中数量，持续高=拥堵）、`active`（正在处理的线程数）。发现 reject 增长就说明写入过载。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 写会被拒？ | 基础 | 线程池满 reject | P5 |
| L2 | 咋兜底？ | 实战 | 429 重试 + bulk 调参 | P6 |
| L3 | 怎么监控？ | 运维 | cat threadpool 三列 | P6+ |
| L4 | queue 高含义？ | 判据 | 写入拥堵 | P7 |
| L5 | bulk 越大越好？ | 反直觉 | 否，易 reject | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| ES 全版本 | 线程池类型命名（write/index）随版本微调，reject 语义稳定 | 答"write 线程池满 reject、429 重试、bulk 调参、cat threadpool 看 reject/queue/active" |

## 关键代码
```go
// Go 侧 bulk 写入：控制批次大小，被拒(429)退避重试
for _, batch := range chunks(docs, 2000) { // 每批 2000 条，别贪大
    _, err := cli.Bulk().Add(batch...).Do(ctx)
    if elastic.IsTooManyRequests(err) { // 429
        time.Sleep(backoff) // 退避后重试，不静默丢
        continue
    }
}
// 监控：GET _cat/threadpool/write?v&h=node,active,queue,rejected
```

## 总结与追问预判
写入有线程池上限与拒绝语义，生产靠"429 重试 + bulk 调参 + cat threadpool 监控"兜底。追问接"副本同步持久性"（136-replica-sync）与"bulk 路由放大优化"（135-bulk-routing-optimization.deep）。

## ⚠️ 原文纠错
1. 事实核校：write 线程池满 reject、429 重试、bulk 调大小/数量/间隔、cat threadpool 三列(reject/queue/active)——均正确 `[经验]`。
2. 崩坏词归一：源码将 Elasticsearch 音译为崩坏词、thread pool 音译为线程状态/现程池、reject 音译为困盈/拒绝、bulk 音译为 bug、queue 音译为队列/排队的崩坏；源码将若干标识符音译为崩坏词，本卡统一为规范术语 `[经验]`。
