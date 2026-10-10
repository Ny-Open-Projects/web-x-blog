# 1419 Kafka 消息堆积 · 深挖

## 思路与架构
消息堆积的本质是「生产速率 > 消费速率」。Kafka 的存储模型把 topic 切成多个 partition，每个 partition 是只追加的日志段（log segment），消费位移（offset）由消费组维护。清理子系统周期性按 retention（时间/大小/起始偏移）裁剪段；当 lag（latest - committed）持续增长且超过 retention 窗口，未消费消息就会被物理删除，造成丢失。因此排查要沿「生产侧速率 → 分区数 → 消费并发 → 单条耗时 → 重平衡」链路定位瓶颈。

## 方案取舍
- **扩容分区 vs 扩容消费者**：分区是并行度上限，消费者数不能超过分区数才有意义；先扩分区再扩消费者。
- **delete vs compact**：delete 保时效、compact 保状态（如最新快照）；状态类数据用 compact，事件流用 delete。
- **重试内联 vs 死信队列**：过多重试拖慢整体，失败消息进死信队列异步处理，主链路不被阻塞。
- **大消息直传 vs 传地址**：图片等大负载走对象存储、Kafka 只传地址，避免占用磁盘/IO 拖慢集群。

## 答题技巧
答堆积题先给因果链「生产>消费→lag 涨→超 retention 丢」，再按六类原因（消费慢/故障重平衡/洪峰/集群故障/分区不合理/消费策略）逐一对应手段。必点 retention 三策略与优先级（ms>minutes>hours）、cleanup.policy 默认 delete；落到方案时强调「分区数≈broker 整数倍、同 key 有序、死信队列隔离、大消息传地址」。追问架构时，用「lag 监控 + 水平扩展 + 死信隔离」收尾。

## 细节与核心 API

**排查与扩容（分区是并行度上限，消费者数不能超过分区数）：**

```bash
# 看 lag（latest - committed）
kafka-consumer-groups.sh --bootstrap-server b:9092 --describe --group g1
# 先扩分区再扩消费者；分区只能增不能减
kafka-topics.sh --bootstrap-server b:9092 --alter --topic t --partitions 12
```

**retention 与清理策略（超窗口未消费即物理删除 → 丢失）：**

```properties
log.retention.hours=168      # retention 优先级 ms > minutes > hours
log.cleanup.policy=delete    # 事件流默认；状态类数据用 compact（保最新快照）
# 大消息直传对象存储、Kafka 只传地址，避免占磁盘/IO 拖慢集群
# 失败消息进死信队列异步处理，主链路不被阻塞
```
