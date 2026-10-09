# 1412 sarama 位移提交：自动/手动配置与窗口机制

> 分类：消息中间件 / Kafka | 难度：L2 | 题型：工程题 | 频率：高 | 关键词：**sarama**/**enable.auto.commit**/**auto.commit.interval**/**MarkMessage**/**重复消费窗口**

> 原文锚点：第 3~17 段「自动提交配置 → 崩溃重放 → 手动提交与 MarkMessage」

## 一句话总述
Kafka 消费位移提交分**自动**与**手动**两档：自动提交把 `Offsets.AutoCommit.Enable` 设 true、按 `AutoCommit.Interval`（sarama 默认 1s 可调）周期性把位移写入 `__consumer_offsets`，编码简单但**崩溃时窗口内未提交的位移会重放**——重复消费不可免；手动提交设 false，在业务处理完成的位置**显式 MarkMessage**，精细可控但要自己写提交逻辑。可靠性哲学（宁重复不丢失）见 `1417-consumer-commit.md`，本卡聚焦 sarama 落地与窗口账本。

## 面试官视角
面试官问这题时手里有张底牌：**自动提交的重复窗口到底多大**。答「可能重复」是及格；能画出「提交周期 t → 拉取 → 消费 → 崩溃」的时间轴、指出重复范围是**上次提交点到崩溃点之间的全部消息**、并给出 interval 调小「缩窗口但费 IO」的量化取舍，才够工程级。再加分的一问是：sarama 的 MarkMessage 和 CommitMessages 是不是一回事——多数人答不上。

## 主问答
**Q（面试官原话）：** 消费者位移提交有哪些方式？

1. **自动提交**：sarama 配置 `Offsets.AutoCommit.Enable = true`（默认），消费者按 `Offsets.AutoCommit.Interval`（默认 1s）周期把已消费位移提交到内部位移主题。优点是**免写提交逻辑**；缺点是**提交时机与业务完成时机脱钩**。
2. **重复消费窗口**：假设 t0 刚提交完，随后拉取一批消息开始处理；t0+1s 的下一次自动提交前程序崩溃——重启后从 t0 位移重新消费，**t0 到崩溃点之间处理过的消息全部重放** [实测] 逻辑推演：窗口上限 ≈ interval + 一批处理时长。
3. **缩窗口的代价**：把 interval 从 1s 调到 100ms，重复范围缩小，但位移提交频率 ×10——每次提交都是对位移主题的一次写入，**挤占 broker 资源并可能触发消费端限流**；且无论调多小都不能归零，窗口只能缩不能灭。
4. **手动提交**：`AutoCommit.Enable = false`，在 `ConsumeClaim` 的消息循环里处理完业务后调 `MarkMessage(msg)`（sarama 的「标记已消费」，由位移管理器按 session 节奏落盘）。优点：**「业务成功」与「位移推进」绑定**，重复风险大幅降低；缺点：提交逻辑自己扛，忘标就是反复重放。
5. **怎么选**：能容忍重复、追求编码简单 → 自动；消息落地数据库/缓存等「处理完才算消费」的场景 → 手动 + 业务成功后标记；可靠性铁律（没成功不提交、消费端幂等）见 `1417-consumer-commit.md`。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | 有哪几种提交方式？ | 说不清自动/手动两档 |
| L2 | sarama 怎么配？ | 说不清 AutoCommit.Enable/Interval |
| L3 | 自动提交为什么会重复？ | 画不出「提交点→崩溃」窗口 |
| L4 | interval 调小能根治吗？ | 说不清「缩窗口不灭窗口」与 IO 代价 |
| L5 | MarkMessage 和 CommitMessages 区别？ | 说不清标记 vs 显式提交的两条路径 |

## 版本与兼容性
| 主题 | 说明 |
|------|------|
| sarama 配置 | `Offsets.AutoCommit.Enable` / `Offsets.AutoCommit.Interval`（默认 1s） |
| 原生 Java 客户端 | 对应 `enable.auto.commit` / `auto.commit.interval.ms`（默认 5s）——面试报 5s 别与 sarama 混 |
| 手动两 API | `MarkMessage` 标记 + session 提交；`CommitMessages` 显式即时提交 |
| 位移存储 | Kafka 0.9+ 存 `__consumer_offsets`（设计见 `1411-offset-topic.md`） |

## 关键代码
```go
cfg := sarama.NewConfig()
cfg.Consumer.Offsets.AutoCommit.Enable = true      // 自动提交
cfg.Consumer.Offsets.AutoCommit.Interval = time.Second

// 手动模式: Enable=false 后, 在 ConsumeClaim 循环里业务成功再标记
func (h handler) ConsumeClaim(s sarama.ConsumerGroupSession, c sarama.ConsumerGroupClaim) error {
	for msg := range c.Messages() {
		if err := handle(msg); err == nil {
			s.MarkMessage(msg, "") // 业务成功才标记位移
		}
	}
	return nil
}
```

## 总结与追问预判
核心：**自动=省事但有不可归零的重复窗口（interval 缩小只能缓解）；手动=业务成功后 MarkMessage，精细但自己扛逻辑**。追问常拐向「重复消费之后怎么办」→ 消费端幂等（唯一键/幂等写入），以及「位移提交与 rebalance 的联动」→ 提交不及时触发重平衡时的重复放大（见 `147-consumer-rebalance.md`、`148-rebalance-process.md`）；可靠性取舍与静默丢失反面见 `1417-consumer-commit.md`，位移主题存储设计见 `1411-offset-topic.md`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文「写北京缓存」为「写 Redis 缓存」的音转；「第三方包 sara」为 sarama；「uconfigure」为 NewConfig。「位移点 autocommit venable」实为 `Consumer.Offsets.AutoCommit.Enable`（sarama 配置结构按官方路径归一）。
2. 事实核校： [经验] 原文说自动提交适用于「可以容忍数据重复消费的场景」方向正确，但需补一句铁律——自动提交还有**丢失面**（提交先于业务完成时，崩溃后消息被跳过），两档风险都要报，只报重复会误导选型。
