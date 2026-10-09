# 1314 Go ES bulk 处理器与内存风险

> 分类：Go · Elasticsearch 写入 | 难度：L4 | 题型：应用题 | 频率：高 | 关键词：**bulk processor**/**workers goroutine**/**三触发条件**/**内存暴涨**/**flush 间隔**
> 原文锚点：第 43~97 段「bulk 处理器启动与提交时机」

## 一句话总述
bulk 处理器后台启 N 个 goroutine 从 channel 取请求批量提交；提交由**三个条件任一满足**触发——文档数(actionsize)、文档大小(requestsize)、周期时间(flush interval)。大文本或高 TPS 下若不控参数，业务内存会暴涨。

## 面试官视角
- 考察意图：懂不懂 bulk 的异步批提交机制，以及它隐藏的内存风险。
- 分档：P5 知 bulk 比单条快；P6 知 workers/三触发条件；P7 知大文档×批量导致内存暴涨、需控 flush。
- 红旗答案：以为 bulk 是「一次发一批」没内存代价；或不知道三条件。
- 惊艳点：量化举例——10MB/文档×1万文档=100GB 怼进内存；TPS 高但 60s 才刷则几百万文档堆内存。

## 主问答
**Q（面试官原话）：** bulk 写入是怎么提交的？有什么坑？
**A：**
1. **启动机制**：初始化 client 后启 bulk processor，它启 workers 个 goroutine，从 channel 逐条取请求。
2. **三触发条件**：满足任一即提交——文档数(actionsize)、文档总大小(requestsize)、周期时间(flush interval)。
3. **默认参数**：workers=3、flush=1s、actions=5、requestsize=5MB；先到者先触发。
4. **afterFunction 回调**：提交后回调捕捉异常、输出错误日志。
5. **内存风险**：大文本(如 10MB/文档)或大批量堆积(高 TPS+长 flush)会大量占业务内存，参数过大则被忽略给合理值保护稳定性。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | bulk 为什么快？ | 基础 | 合并请求减网络往返 | P5 |
| L2 | 哪三条件触发提交？ | 机制 | 数量/大小/时间任一 | P6 |
| L3 | workers 是什么？ | 原理 | 后台消费 goroutine 数 | P6 |
| L4 | bulk 内存风险？ | 风险 | 大文档×批量占内存 | P7 |
| L5 | 参数过大怎么处理？ | 进阶 | 忽略给合理值，保护稳定 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| olivere/elastic v7 | BulkProcessor 为该 SDK 组件 | 官方 SDK 用 esutil.BulkIndexer，概念一致（workers/批量/刷新间隔） |

## 关键代码
```go
// olivere/elastic：三条件触发
p, _ := elastic.NewBulkProcessorService(cli).
    Workers(3).
    BulkActions(5).      // actionsize：文档数
    BulkSize(5<<20).     // requestsize：5MB
    FlushInterval(1 * time.Second). // 周期
    After(func(_ int64, _ []elastic.BulkResponseItem, err error) { /* 日志 */ }).
    Do(ctx)
p.Start(ctx)
p.Add(elastic.NewBulkIndexRequest().Index("idx").Doc(doc))
```

## 总结与追问预判
bulk 是「异步批提交」，收益在减网络往返，代价在内存缓冲——必须按文档大小与 TPS 调三参数。下一步常问文档/索引操作的 API。

## ⚠️ 原文纠错
1. 事实核校： [经验] workers goroutine 消费 channel、三触发条件任一即提交、默认 workers=3/flush=1s/actions=5、afterFunction 回调、大文档内存风险——均正确。
2. 崩坏词归一：源码将 bulk 音译为 bug（本卡统一为 bulk）、goroutine 音译为携程、Do 方法 音译为「丢方法」、work 方法 音译为 worp、Add 方法 音译为艾/艾特、bulk service 音译为 backservice；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
