---
title: [NODE-648] 进程守护与崩溃自愈（uncaughtException）怎么做？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-648：崩溃自愈怎么做？
**答**：
- 崩溃语义：uncaughtException = 状态可能已损坏（官方不建议继续运行）——正确做法：记录（含堆栈+最近请求上下文）→ 快速退出 → 进程守护拉起（cluster fork/PM2/K8s restart）——「崩溃即重启」优于「带病运行」。
- 分级决策：可识别可恢复的错误（连接重置）→ 错误处理不冒泡；未知异常 → 优雅退出（SCN-NODE-638 优雅关闭走一遍——排空再退）+ 崩溃日志先行落盘（同步写——崩溃时异步日志可能丢）。
- 崩溃风暴防御：连续崩溃重启限流（PM2 min_uptime/max_restarts——backoff，SCN-SLA-763 重试风暴同源）；崩溃循环告警（重启 > N 次/分钟 = 系统性故障）。
- 崩溃上下文保留：最近请求环形缓冲（黑盒记录仪——崩溃前最后 N 个请求快照进日志，复现线索）。
- 追问钩子：为什么崩溃前要「同步写日志」——进程退出时异步日志缓冲区未 flush 就丢了（sonic-boom 异步写的代价）；崩溃路径上 fs.writeFileSyncSync 强制落盘（性能不重要了，数据不能丢）——「正常路径异步、崩溃路径同步」是日志双轨制。

```javascript
process.on('uncaughtException', async (err) => {
  fs.writeFileSyncSync('crash.log', JSON.stringify({
    err: err.stack, lastRequests: ringBuffer.last(10), ts: Date.now() }));   // 同步落盘
  await gracefulShutdown(5_000);                       // 尽力优雅（5s 超时）
  process.exit(1);                                     // 交给守护拉起
});
// PM2: max_restarts: 10, min_uptime: '10s'            // 崩溃风暴限流
```
