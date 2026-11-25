---
title: [MFW-809] Server Action 长事务未提交时，流式渲染的 Suspense 边界该何时 flush
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-809：Server Action 长事务未提交时，流式渲染的 Suspense 边界该何时 flush

**答**：
- 结论：渲染 flush 由 Suspense 调度决定，与 action 事务提交是两个独立时钟；不要让渲染等待长事务提交，否则首屏被拖住。
- 做法：长事务用 action 异步执行并立即返回「已受理」，UI 乐观更新 + 后续 revalidate；渲染侧只读已提交快照。
- 追问钩子：如果页面必须展示事务结果呢？——用轮询/SSE 推送事务状态，而不是让渲染阻塞等提交。

```javascript
// 长事务 Action：立即受理，不阻塞响应
async function submitBatch(rows) {
  'use server';
  const jobId = await jobs.enqueue(rows);          // 落队列
  return { jobId, state: 'ACCEPTED' };
}

// 页面渲染：只读已提交快照，不被长事务阻塞
async function ReportPage() {
  const snapshot = await db.reports.latest();      // 独立读
  return <Suspense fallback={<Skeleton/>}>
    <Report data={snapshot} />
  </Suspense>;
}

// 客户端：乐观更新 + SSE 接收事务进度
function onSubmit(res) {
  showOptimistic();
  const es = new EventSource('/api/job/' + res.jobId + '/events');
  es.onmessage = (e) => { if (JSON.parse(e.data).done) router.refresh(); };
}
```
