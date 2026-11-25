---
title: [MFW-569] 元框架与消息队列：Action 的异步任务委派
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-569：Action 的异步任务委派

**答**:
- Action 的执行约束：serverless 有时长上限（Vercel 10s-60s——长任务必须委派）；「Action 只做编排、重活进队列」：action 里入队（BullMQ/QStash/SQS）→ 立即返回任务 id → client 轮询/订阅进度。
- 进度反馈的形态：1) 轮询（route handler 查任务状态——简单可靠）；2) SSE 推送（任务 worker 完成 → Redis pub/sub → SSE 推 client——实时但连接管理成本）；3) Action 的 streaming 返回（createAsyncIterable——action 响应保持打开流式输出进度——serverless 限制内）。
- 任务结果的回传：worker 完成后写 DB + revalidate（worker 无法调 Next revalidate（serverless 外）——通过 API 触发 revalidate（webhook to route handler——队列 worker → revalidate 端点））。
- 幂等与任务去重（RBL-568 的队列版）：任务 id = idempotencyKey（重复入队去重）。
- 追问钩子：为什么「worker 里不能直接 revalidateTag」而要绕 API？——revalidateTag 操作的是「Next 进程内的缓存状态」（Full Route Cache 在部署平台的函数实例内）；worker 是独立进程（无 Next 上下文）——跨进程失效只能走「HTTP 触发」（Next 的 revalidate 端点：cache-life 管理通过 API 面）——「缓存失效的进程边界」：进程内 API vs 跨进程 HTTP 的切换点，与分布式缓存失效（RBL-637）同构。

```typescript
// Action 入队（编排）
'use server';
export async function generateReport(formData: FormData) {
  const taskId = crypto.randomUUID();
  await fetch(QSTASH_URL, { method: 'POST',
    headers: { 'Upstash-Delay': '0s', Authorization: `Bearer ${QSTASH_TOKEN}` },
    body: JSON.stringify({ taskId, type: 'report', params: {...} }),
  });                                                    // 入队立即返回
  return { taskId };                                     // client 拿 id 轮询
}
// 进度查询 route handler
export async function GET(req: Request) {
  const id = new URL(req.url).searchParams.get('id');
  const task = await db.tasks.find(id);
  return NextResponse.json({ status: task.status, progress: task.progress });
}
// worker 完成后触发 revalidate（跨进程）
// worker: await doHeavyWork();
// worker: await fetch(`${NEXT_URL}/api/revalidate?tag=report-${taskId}`, { method: 'POST' });
// /api/revalidate/route.ts: revalidateTag(tag)  ← 队列完成 → 缓存失效闭环
```
