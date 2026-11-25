---
title: [NODE-657] 分布式 ID 生成怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-657：分布式 ID 怎么做？
**答**：
- 方案谱系：UUID v4（无序——索引差）、雪花 Snowflake（时间戳+机器+序列——趋势递增，时钟回拨问题）、号段模式（DB 批量取段——简单可控）、Redis INCR（简单但 Redis 单点）。
- 雪花时钟回拨：机器时钟回退会生成重复 ID——回拨小则等待、回拨大则告警+拒绝；时钟监控（NTP 漂移检测）是前置。
- 趋势递增的价值：DB 索引友好（B+ 树顺序插入——UUID 随机写是索引碎片化来源）；趋势递增不等于连续（暴露量——对外加密映射）。
- 选型：内部系统号段（简单）；跨服务高并发雪花（需机器 ID 分配——K8s stateful 序号/env 注入）。
- 追问钩子：为什么「机器 ID 分配」是雪花方案落地的真正难点——算法本身简单，难点在「机器 ID 全局唯一且重启不变」：手动配置会漂移（误配重复→ID 重复）、K8s 动态 IP 不可靠；解法是启动时向协调服务注册领取（zk/DB 表+租约）或 stateful 有序分配——ID 重复是静默数据事故，分配机制必须工程化。

```javascript
// 雪花 + 时钟回拨防护
let lastTs = 0;
function nextId() {
  let ts = Date.now();
  if (ts < lastTs) {                                    // 回拨
    if (lastTs - ts < 100) { while ((ts = Date.now()) <= lastTs); }   // 小回拨等待
    else throw new Error('CLOCK_BACKWARD');             // 大回拨拒绝
  }
  lastTs = ts;
  return (BigInt(ts - EPOCH) << 22n) | (machineId << 12n) | seq();
}
```
