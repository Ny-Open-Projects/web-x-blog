# 1419 Kafka 日志清理：时间/大小/偏移三策略

> 分类：消息中间件 / Kafka | 难度：L4 | 题型：原理题 | 频率：中 | 关键词：**cleanup.policy、retention.ms、retention.bytes、logStartOffset、delete/compact**

> 原文锚点：第 8~28 段「log.cleanup.policy 默认 delete…retention.ms 优先级最高、retention.minutes 次之…retention.bytes 总大小限制…起始偏移量 logStartOffset 可手动删段」

## 一句话总述
Kafka 用专门的删除任务周期裁剪日志段，保留策略三类：**基于时间**（retention.ms 优先级最高）、**基于大小**（retention.bytes 总大小上限）、**基于起始偏移**（logStartOffset 手动指定删段）。默认保留 7 天。

## 面试官视角
P6 能说出三类策略；P7 要讲清 retention 三配置的优先级（ms > minutes > hours），以及 logStartOffset 本质是「手动指定要删的段起点」，可精确删除。

## 主问答
**Q（面试官原话）：** 消息达到什么条件会被清理？

1. **时间策略**：`retention.ms` 优先级最高，次之 `retention.minutes`、再次 `retention.hours`；默认 168（即 7 天）`[源码]`。
2. **大小策略**：`retention.bytes` 限制所有日志总大小，超了从第一个段开始删；默认 -1 不限制 `[源码]`。
3. **单段上限**：`segment.bytes` 控制单个日志段最大；计算差值后从首段向后查找可删集合 `[经验]`。
4. **偏移策略**：`logStartOffset` 一般是首段 baseOffset，可用脚本/接口改它，起点小于它的段被删 `[源码]`。
5. **优先级取值**：时间戳优先取索引最后一条；为零才取文件最后修改时间 `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 几种策略？ | 答不出时间/大小/偏移 |
| L2 | 时间优先级？ | 说不出 ms>minutes>hours |
| L3 | 默认保留？ | 答不出 7 天 |
| L4 | 偏移怎么用？ | 答不出手动删段 |
| L5 | 单段上限？ | 答不出 segment.bytes |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Kafka 全版本 | 三策略并存 | 时间/大小/偏移 |
| 任意版本 | 时间优先级固定 | ms 最高 |
| 任意版本 | 默认 7 天 | retention.ms=168h |

## 关键代码
```go
adm, _ := sarama.NewClusterAdmin(addrs, cfg)
// 同 key 仅留最新值，且仍按时间删过期段
adm.AlterConfig(sarama.TopicResource, "order", map[string]*string{
    "cleanup.policy": ptr("delete,compact"),
    "retention.ms":   ptr("604800000"), // 7 天
}, false)
```

## 总结与追问预判
**清理策略决定「堆积多久会丢」**。回到堆积极限——见同批 1419-backlog-impact 与 1419-backlog-causes。

## ⚠️ 原文纠错
1. 事实核校：三类保留策略、retention.ms 优先级最高、默认 7 天、logStartOffset 手动删段——均准确 `[经验]`。
2. 补充：原文「默认日志段保留 7 天」精确是 retention.ms 默认 168 小时，且以索引时间戳优先 `[经验]`。
3. 崩坏词归一：源码将 Kafka、broker、配置项等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
