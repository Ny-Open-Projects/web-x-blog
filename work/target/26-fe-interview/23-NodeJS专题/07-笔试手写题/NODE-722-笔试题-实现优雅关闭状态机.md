---
title: [NODE-722] 笔试题——实现优雅关闭状态机（排空 + 超时 + 顺序）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-722：手写优雅关闭状态机

**需求与边界**：
- 需求：SIGTERM → 状态机 RUNNING → DRAINING（停收新请求）→ CLEANING（关连接池）→ EXITED；① 排空带超时兜底（30s 强制——防僵尸）；② 重复信号幂等（二次 SIGTERM 不重复流程）；③ 强杀兜底（超时后 process.exit(1)）。

**答**：
```javascript
function gracefulShutdown(server, cleanup, { drainMs = 30_000 } = {}) {
  let state = 'RUNNING';
  let shuttingDown = false;                            // 幂等（SCN-NODE-638）
  async function shutdown(signal) {
    if (shuttingDown) return;                          // 重复信号幂等
    shuttingDown = true; state = 'DRAINING';
    server.close(() => state = 'CLEANING');            // 停收新请求 + 排空
    const drained = await Promise.race([
      waitFor(server, 'close'),
      sleep(drainMs).then(() => false),                // 超时兜底
    ]);
    if (!drained) forceCloseConnections();             // 强制断开在途（log）
    state = 'CLEANING';
    await cleanup();                                   // 连接池/消费者关闭（SCN-NODE-638 顺序）
    await flushTelemetry();                            // 最后 flush
    state = 'EXITED';
    process.exit(0);
  }
  process.on('SIGTERM', () => shutdown('SIGTERM'));
  process.on('SIGINT', () => shutdown('SIGINT'));
  // 超时强杀兜底（防排空永不完成）
  setTimeout(() => { if (state !== 'EXITED') process.exit(1); }, drainMs + 10_000).unref();
  return { get state() { return state; } };
}
```

**评分点**:
- 状态机三态 + 重复信号幂等。
- 排空 Promise.race 超时兜底 + 强制断开（SCN-NODE-638 排空语义）。
- 关闭顺序（排空→连接池→遥测 flush 最后）。
- 外部强杀兜底（drainMs + 10s unref——不阻止正常退出）。
