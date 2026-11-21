---
title: [NODE-306] worker 深水区：任务分级与抢占？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-306：worker 深水区：任务分级与抢占？
**答**:
- 问题：worker 池被长任务占满，紧急任务排队——需要分级调度。
- 方案：池内优先级队列（DP-343 同款）+ 独立高优先池（1~2 个 worker 专跑 urgent）；长任务拆片（可中断任务用分批 postMessage 汇报进度，主线程可 terminate 换优先级）。
- JS 无真正抢占：worker 内长循环无法被外部打断——只能靠任务自觉检查 abort signal（循环内 signal.aborted 退出）。
- 监控：分级队列长度与等待 P95——urgent 队列 > 0 持续即告警。

```javascript
// 分级池 + 可中断任务
const urgentPool = new Piscina({ maxThreads: 2 });   // 专用高优池
const normalPool = new Piscina({ maxThreads: 6 });
function run(task, { priority = 'normal' } = {}) {
  return (priority === 'urgent' ? urgentPool : normalPool).run(task.data, { signal: task.signal });
}
// worker 内协作式中断（task.js）
parentPort.on('message', async ({ data, signalPort }) => {
  for (let i = 0; i < 1e6; i++) {
    if (signalPort.aborted) return parentPort.postMessage({ aborted: true });   // 每步检查
    step(i);
  }
});
```
