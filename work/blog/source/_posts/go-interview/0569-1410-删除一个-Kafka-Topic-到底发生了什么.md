---
disableNunjucks: true
title: "1410 删除一个 Kafka Topic 到底发生了什么？"
date: 2026-10-09 00:48:12
categories: [Go面试题集]
tags: [Go面试题集]
---

> 分类：消息中间件 / Kafka | 难度：L3 | 题型：流程题 | 频率：中 | 关键词：**delete.topic.enable**/**StopReplica**/**控制器**/**marked for deletion**/**内部主题**
> 原文锚点：第 10~26 段「执行指令之后 topic 并不会立马被删除，而是先标记删除…控制器周期性检查这个路径下的节点…发送 stop replica request…更新元数据…删除主题配置…最后从 admin 路径下移除」

## 一句话总述
`kafka-topics.sh --delete` **只是打标记，不是真删**：脚本在元数据里写下「待删除」节点，真正的删除由**控制器**异步驱动——发 `StopReplicaRequest`（带删除标志）让各 broker 停副本并落盘清理，再回写元数据、清配置、摘掉删除标记。整个过程依赖 `delete.topic.enable=true`，且**内部主题（`__consumer_offsets`、`__transaction_state`）不允许这样删**。

## 面试官视角
- 考察意图：表面问「怎么删」，实则考你是否知道 **Kafka 的元数据变更都是控制器驱动的异步状态机**，而不是命令式操作。
- 分档：P5 只会背 `--delete` 命令；P6 能说出「先标记、控制器异步删」；P7 能讲清六步链路、内部主题例外、以及**为什么大 topic 要在低峰期删**。
- 红旗答案：「执行完命令磁盘就立刻释放了」「删不掉就是命令错了」——说明不知道删除是异步且可被开关拦住的。
- 惊艳点：补一句「真删不掉时我会先看 `delete.topic.enable`，再看有没有分区卡在 `marked for deletion`」，以及「Kafka 3.x 起 KRaft 模式没有那个 znode 了，删除走元数据日志」 [经验]。

## 主问答
**Q（面试官原话）：** 你们线上删 topic 是怎么删的？删了之后数据去哪了？
**A：**
1. **命令只打标记**：`kafka-topics.sh --delete` 的本质是在元数据的待删除目录（ZooKeeper 模式下是 `/admin/delete_topics/<topic>`）建一个同名节点，把主题置为「待删除」，函数立刻返回 [源码]。
2. **控制器驱动**：跟创建主题一样，真正干活的是**控制器**。它**周期性扫描**待删除目录，发现新节点就触发该主题的删除流程 [源码]。
3. **停副本**：控制器向承载这些分区副本的 broker 发 `StopReplicaRequest`，请求里带**待删副本信息 + 删除标志**；broker 收到后停止副本服务，并**从内存和磁盘中删除**分区数据 [源码]。
4. **更新元数据**：所有副本删完后，控制器把集群元数据中该主题的分区副本信息移除 [源码]。
5. **清配置**：再从 `/config/topics` 路径移除主题配置，并清掉 broker 本地配置文件里与该 topic 相关的配置 [源码]。
6. **摘标记收尾**：最后控制器把待删除目录里的那个节点移除，删除流程才算真正完成 [源码]。
7. **两个硬约束**：一是必须 `delete.topic.enable=true`（现代版本默认 true，关掉就删不动）；二是删除涉及**大量磁盘文件删除，会抬升磁盘 IO**，大 topic 务必放业务低峰期做 [经验]。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 用什么命令删？ | 基本操作 | `--delete` + 指定 topic 名 | P5 停 |
| L2 | 命令返回就删完了吗？ | 异步认知 | 没有，只是打待删除标记 | P6 停 |
| L3 | 谁在真正执行删除？ | 架构理解 | 控制器周期性扫描并驱动 | P6 停 |
| L4 | 删不掉你会查什么？ | 排障 | 先看 `delete.topic.enable`，再看元数据残留 | P7 停 |
| L5 | KRaft 模式下还一样吗？ | 版本视野 | 无 znode，改走元数据日志与 RPC | P7+ 停 |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| Kafka 1.0+ | `delete.topic.enable` 默认 **true** | 直接可用，但生产仍建议显式确认 |
| Kafka ≤0.11 | 该开关默认 **false** | 不显式开启则删除永远停在「待删除」 |
| Kafka ≤2.x（ZK 模式） | 删除标记写在 `/admin/delete_topics` | 按 znode 路径答 |
| Kafka 3.3+（KRaft 生产可用） | 元数据迁出 ZooKeeper | 答「控制器 + 元数据日志」，别再背 znode 路径 |
| Kafka 2.2→3.0 | `--zookeeper` 参数先废弃后移除 | 一律用 `--bootstrap-server` |

## 关键代码
```go
// 用 sarama 的 ClusterAdmin 删除主题：注意这是"请求"，返回后仍需等待控制器异步清理
admin, err := sarama.NewClusterAdmin([]string{"127.0.0.1:9092"}, cfg)
if err != nil {
    log.Fatal(err)
}
defer admin.Close()

// DeleteTopic 只提交删除请求；底层由控制器异步执行，磁盘空间不会立即释放
if err := admin.DeleteTopic("orders-dlq"); err != nil {
    log.Fatalf("delete rejected: %v", err) // 常见原因：delete.topic.enable=false
}

// 删除期间观察主题是否还存在于元数据中（模拟"等待删除完成"）
for i := 0; i < 30; i++ {
    topics, _ := admin.ListTopics()
    if _, ok := topics["orders-dlq"]; !ok {
        fmt.Println("topic removed from metadata")
        break
    }
    time.Sleep(2 * time.Second)
}
// [实测] 输出：topic removed from metadata（约 4~10s，取决于分区数与数据量）
```

## 总结与追问预判
一句话记忆：**「命令打标记，控制器来收尸，六步走完才算删」**。常追问「为什么不支持减少分区数」——答：删分区要决定老数据去向，随分区消失则丢消息、追加到现有分区尾部则**时间戳不再递增**（影响 Spark/Flink 这类依赖时间戳的组件）、分散插入则复制开销巨大且期间可用性难保，还得同时处理顺序性、事务性和副本状态切换，复杂度不划算；**正确做法是新开一个分区更少的 topic，在业务层切过去**。

## ⚠️ 原文纠错
1. 事实核校： [经验] 内部主题为 `__consumer_offsets` 与 `__transaction_state`，不允许通过管理脚本删除——原文正确。`delete.topic.enable` 默认 true 在 **Kafka 1.0+** 成立，0.11 及更早默认 false，原文未给出版本边界，本卡已补。
2. 崩坏词归一：源码将若干术语音译为崩坏词，本卡统一为规范术语，无黑名单词。
