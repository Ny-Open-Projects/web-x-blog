---
title: [TST-843] 前端内存泄漏的自动化测试如何做？（detached nodes / 监听器累积）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-843：前端内存泄漏的自动化测试如何做？（detached nodes / 监听器累积）
**答**：
- 结论：内存泄漏测试的核心是「同一操作重复 N 次后，堆内存/节点数/监听器数不应持续增长」——对比基线而非看绝对值。
- 检测手段：Chrome DevTools Protocol 取 JSHeapUsedSize、DOM 节点数、监听器数（getEventListeners），执行操作→GC→再测，重复多轮看趋势。
- 常见泄漏源：未解绑的事件监听、未 clear 的定时器、闭包持有 DOM、全局缓存无限增长。
- 门禁化：把「N 轮后堆增长 < 阈值」做成 CI 任务，配合 --expose-gc 强制回收以稳定测量。
- 追问钩子：GC 后内存仍不降，一定是泄漏吗？如何区分「真的是泄漏」和「V8 还没来得及回收」？

```javascript
// 内存泄漏检测：重复操作后对比堆大小
async function detectLeak(page, action, rounds = 10) {
  const heap = [];
  for (let i = 0; i < rounds; i++) {
    await action(page);
    await page.evaluate(() => window.gc && window.gc()); // 需 --expose-gc
    const m = await page.metrics();
    heap.push(m.JSHeapUsedSize);
  }
  const growth = (heap[heap.length - 1] - heap[0]) / heap[0];
  return { growth: Number(growth.toFixed(3)), leak: growth > 0.2 };
}
// 打开模态框又关闭，重复 10 次，堆不应持续增长
detectLeak(page, async p => {
  await p.getByText('打开').click();
  await p.getByText('关闭').click();
});
```
