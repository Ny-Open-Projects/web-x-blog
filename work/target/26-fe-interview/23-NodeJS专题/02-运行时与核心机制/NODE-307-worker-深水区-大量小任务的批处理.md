---
title: [NODE-307] worker 深水区：大量小任务的批处理？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-307：worker 深水区：大量小任务的批处理？
**答**:
- 问题：1 万个 5ms 任务逐个进 worker——通信开销（序列化+调度）占总耗时一半。
- 批处理：任务在主线程攒批（N 条或 10ms 窗口）→ 一次 postMessage 批量 → worker 内循环处理 → 一次回传批量结果；结果按 id 关联分发。
- 进一步：任务代码热路径留在 worker 常驻（workerData 初始化一次），消息只传数据。
- 收益量化：通信次数从 N → N/batchSize；实测小任务吞吐提升 5~10x。

```javascript
// 批处理 worker 通信
const batch = [];
let timer;
function submit(task) {
  return new Promise((resolve, reject) => {
    batch.push({ ...task, resolve, reject });
    if (batch.length >= 50) flush();              // 数量触发
    timer ??= setTimeout(flush, 10);              // 10ms 窗口触发
  });
}
function flush() {
  clearTimeout(timer); timer = null;
  const jobs = batch.splice(0);
  worker.postMessage({ jobs: jobs.map(j => j.data) }, jobs.map(j => j.transfer).filter(Boolean));
  // worker 回传 { id, result }[] → jobs.forEach(j => j.resolve(byId.get(j.id)))
}
```
