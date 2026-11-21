---
title: "G11. Redis 延迟队列/pipeline？（追问补齐）"
date: 2026-11-18
categories: [Java面试, 追问地图]
tags: [Java面试, 补漏卡, 33]
type: 补漏卡
disableNunjucks: true
---

### G11. Redis 延迟队列/pipeline？（追问补齐）

**【参考回答（可背）】** ① **ZSet 延迟队列**：score 存执行时间戳，消费端每秒 ZRANGEBYSCORE key 0 now LIMIT n → 取到即 ZREM（**原子性**：多消费者并发 ZREM 只有成功者执行——Lua 封装"取+删"两步防竞争）；可靠性：ZREM 成功后写"任务表"再执行，崩溃重启扫任务表补偿。② **pipeline**：攒 N 条命令一次发送（省 N-1 次 RTT），但**不保证原子**（与 Lua 的区别）；大批量导入用它，原子需求用 Lua（呼应 6.7.2）。③ 对比：毫秒级精度+轻量用 ZSet；任意精度/海量用 RocketMQ 时间轮（第 7 章）；本地内存级用 Netty 时间轮。
**【追问链】** ZSet 方案的缺点？→ 轮询空转耗 CPU（sleep 控制）、无 Ack 机制（崩溃即丢，需任务表补偿）、堆积无背压——所以"有 MQ 就别用 Redis 做延迟队列"。
