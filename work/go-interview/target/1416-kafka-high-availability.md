# 1416 Kafka 高可用：五支柱机制全景

> 分类：消息中间件 / Kafka | 难度：L2 | 题型：原理题 | 频率：高 | 关键词：**集群模式**/**ZooKeeper**/**控制器选举**/**副本机制**/**故障转移**/**动态扩容**

> 原文锚点：第 2~13 段「集群模式 → ZooKeeper → 副本机制 → 故障检测 → 动态扩容」

## 一句话总述
Kafka 高可用五支柱：① **集群模式**（多 broker 分布式存储+复制+负载均衡）；② **ZooKeeper 协调层**（管元数据、控制器选举，≥3 节点自身高可用）；③ **副本机制**（每分区多副本，leader 处理读写、follower 同步，leader 挂则从 follower 选举新 leader）；④ **故障检测与转移**（心跳监控 broker 健康，自动选主+副本同步）；⑤ **动态扩容**（加 broker/加分区/重平衡分配）。ISR 细节与重平衡流程见 `147-isr-replication.md`/`148-rebalance-process.md`，本卡给五支柱全景。

## 面试官视角
HA 题考的是**机制间的分工关系**而非名词罗列：ZooKeeper 管「控制面」（谁是控制器、元数据），副本机制管「数据面」（分区的读写与冗余）——两层各司其职。两个分水岭：① 控制器和分区 leader 是**两级选举**，混为一谈即暴露没理清；② 追问「**没有 ZooKeeper 行不行**」——KRaft（Raft 元数据仲裁）3.3+ 生产可用、4.0 起彻底移除 ZK，版本边界意识直接定档。

## 主问答
**Q（面试官原话）：** Kafka 是如何实现高可用的？

1. **集群模式**：多 broker 分布在不同机器，数据复制+分区负载均衡——单点故障不影响整体，扩展性与可用性同源。
2. **ZooKeeper 协调层**：管理集群元数据（broker/topic/分区）；ZK 自身 leader/follower/observer 三角色（observer 不投票），**至少 3 节点**部署保证自身高可用。Kafka 的**控制器（controller）选举依赖 ZK**——当选控制器临时登记在 ZK；控制器本质是某个「兼职特殊职责」的 broker，负责分区 leader 选举与副本同步管理；控制器挂了自动从其余 broker 重选。
3. **副本机制（数据面 HA）**：每分区多副本跨 broker 分布——leader 处理读写，follower 同步数据；leader 故障则从 follower 中**选举新 leader**，分区持续可用。与 ES 主分片/副本分片同构（见 `137-segment-merge.md` 所在的 ES 专题对照）。
4. **故障检测与转移**：心跳+检测机制监控 broker 健康；判定故障后触发故障转移——选新 leader、副本同步追平，恢复服务。
5. **动态扩容与重平衡**：支持在线加 broker、加分区、调分配策略；broker 集合变化时**自动重平衡**把分区重分配到新节点（这里的 rebalance 是**分区分配重平衡**，与消费组 rebalance 是两码事，别混——后者见 `148-rebalance-process.md`）。
6. **[经验] 版本边界主动补**：KRaft 模式（Kafka 自身用 Raft 管元数据）3.3+ 生产可用，**4.0 起彻底移除 ZooKeeper**——答 ZK 时必须带这句，否则显得认知停留在旧版本。

## 追问链
| 档位 | 追问 | 答不出停在哪档 |
|------|------|----------------|
| L1 | Kafka 高可用靠什么？ | 五支柱报不全 |
| L2 | 副本机制怎么工作？ | leader/follower 读写与同步说不清 |
| L3 | 控制器是什么？谁选的？ | 与分区 leader 两级选举混淆 |
| L4 | ZK 为什么至少 3 节点？ | 说不清过半选举机制 |
| L5 | 没有 ZooKeeper 行吗？ | 不知道 KRaft 与 4.0 移除 |

## 版本与兼容性
| 主题 | 说明 |
|------|------|
| 副本机制 | leader 读写 / follower 同步 / ISR 追赶（见 147-isr-replication） |
| 控制器 | 单例特殊 broker；ZK 选举（旧）/ KRaft Raft 仲裁（新） |
| ZooKeeper | ≥3 节点；leader/follower/observer（observer 不投票） |
| KRaft | 3.3+ 生产可用；4.0 移除 ZK |
| 两类 rebalance | 分区分配重平衡 vs 消费组 rebalance，机制无关 |

## 关键代码
```go
// 两级选举决策矩阵 (规则示意, 对齐 Kafka HA 语义)
type Broker struct {
	ID           int
	IsController bool
	InISR        bool
}

// electPartitionLeader: 控制器从 ISR 中选新 leader; ISR 全空按 unclean 开关
func electPartitionLeader(replicas []Broker, unclean bool) string {
	for _, r := range replicas {
		if r.InISR {
			return fmt.Sprintf("新 leader = broker-%d (ISR 内)", r.ID)
		}
	}
	if unclean {
		return "unclean 开启: 从非 ISR 副本选 -> 可能丢已 ack 消息"
	}
	return "unclean 关闭 (默认): ISR 全下线 -> 分区停写, 宁停不丢"
}
```

[实测] 输出：ISR 正常选 broker-2；ISR 全灭 + unclean 关 = 停写；unclean 开 = 可能丢消息。

HA 两层分工总览：
```text
Kafka HA 两层分工 (控制面 vs 数据面)
├─ 控制面 (谁管事?)
│   ├─ ZooKeeper/KRaft: 元数据 + 控制器选举
│   ├─ 控制器(特殊 broker): 分区 leader 选举/副本同步管理
│   └─ 控制器故障 -> 其余 broker 重选新控制器
├─ 数据面 (数据怎么活?)
│   ├─ 分区多副本跨 broker
│   ├─ leader 读写, follower 同步
│   └─ leader 故障 -> follower 中选新 leader (ISR 内优先)
├─ 故障检测: 心跳监控 -> 故障转移
└─ 扩容: 加 broker/分区 -> 分区分配重平衡
```

## 总结与追问预判
核心：**五支柱 + 两层分工（ZK/控制器管控制面、副本机制管数据面）+ KRaft 版本边界**。追问常往深走——ISR 收缩扩张与 acks 配合见 `147-isr-replication.md`/`1417-producer-acks.md`、消费组重平衡流程见 `148-rebalance-process.md`/`147-consumer-rebalance.md`、写流程与副本落盘见 `147-write-flow.md`/`147-kafka-write-flow.deep.md`，高可用答题战术见 `142-mq-answer-tactics.md`。

## ⚠️ 原文纠错
1. 术语核校： [经验] 原文「卡夫卡」=Kafka、「brokertopic」=broker/topic 转写粘连、「d的副本/追随着」=leader/follower 音转，已归一。
2. 事实核校： [经验] 原文通篇以 ZooKeeper 为唯一元数据方案——需补版本边界：**KRaft 模式 3.3+ 生产可用、4.0 起移除 ZK**，控制器选举改由 Raft 仲裁完成；「控制器选举依赖 ZooKeeper」仅在旧版本成立。
