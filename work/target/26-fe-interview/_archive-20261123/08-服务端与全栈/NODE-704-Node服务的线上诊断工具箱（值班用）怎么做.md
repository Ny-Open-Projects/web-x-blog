---
title: [NODE-704] 线上诊断工具箱（值班用）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-704：诊断工具箱怎么做？
**答**：
- 值班工具集：heapdump 信号（kill -USR2——SCN-NODE-672）、CPU profile 信号（SIGUSR1——inspector 激活）、运行时状态接口（内部端点：事件循环延迟/内存/连接池水位/队列积压——SCN-NODE-671 遥测聚合的值班视图）、诊断脚本（连接池泄漏检查/慢查询快照）。
- 工具安全：诊断端点内网-only（鉴权 + 网络隔离——外网暴露是事故）、高开销操作摘流执行（SCN-NODE-671 纪律）。
- 一键诊断：综合诊断端点（一键收集：heap/延迟/池/最近错误——值班 5 分钟出全貌，SCN-OPS-192 一键诊断同源）。
- 工具箱文档化：每个工具的「什么时候用/怎么用/怎么解读」——工具没文档等于没有（SCN-OPS-183 runbook 联动）。
- 追问钩子：为什么诊断端点要「内网 only」——heap dump 含内存全量数据（敏感信息/密钥可能驻留）、运行时状态暴露攻击面（连接池水位=容量信息）；诊断能力是给值班人的，不是给攻击者的——内网隔离 + 鉴权双闸是诊断能力的存在前提。

```javascript
// 内网诊断端点（值班工具箱）
app.get('/internal/diag', internalOnly, async (req, res) => {
  res.json({
    eld: eldP99(), mem: process.memoryUsage(), pools: poolStats(),
    queues: queueDepths(), recentErrors: ringBuffer.last(20),   // 一键全貌
  });
});
process.on('SIGUSR2', () => heapdump.write());         // heapdump 信号
```
