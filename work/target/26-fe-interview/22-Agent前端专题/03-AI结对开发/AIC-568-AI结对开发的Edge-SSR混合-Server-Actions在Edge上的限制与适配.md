---
title: [AIC-568] Server Actions 在 Edge 的限制与适配
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-568：Server Actions 在 Edge 的限制

**答**:
- Server Actions 在 Edge 运行时的限制（RBL-761 的 Action 维度）：1) **执行时间限制**（Edge 通常 30s 上限——Action 的长操作（报告生成/批量处理）超限 → 需要委派到队列（RBL-569）；2) **无 Node API**（fs/crypto 完整/child_process——Action 中不能用 Node 模块（RBL-787 的 API 审计）；3) **无持久连接**（DB 直连受限——HTTP driver RBL-517；4) **无文件系统**（无 fs.writeFileSync——文件操作走对象存储（S3 presign RBL-592）；5) **内存限制**（128MB——大数据处理受限 RBL-787）。
- Action 的适配策略：1) **轻操作在 Edge**（CRUD/查询/表单验证——< 30s < 128MB）；2) **重操作委派**（批量/报告/文件处理 → 队列 + Worker（RBL-569 的 Edge 版——Action 入队 → 独立 Worker 消费）；3) **混合部署**：某些 Action 在 Edge（轻）某些在 Node（重）——per-route runtime 声明 RBL-575。
- 追问钩子：为什么「Server Action 的 Edge 限制」影响架构设计而非仅部署选择？——Edge 的限制（30s/128MB/无 Node）意味着「某些功能无法在 Edge 实现」（文件处理/长时间计算）——架构必须适配：重操作委派到队列（Agent 的异步模式 RBL-518）或用 Node runtime 的路由；「Edge 的约束 = 架构的约束」：不是"部署后看看有没有问题"而是"设计时就考虑 Edge 限制"（RBL-620 渲染决策树的 runtime 维度）。

```typescript
// Edge 上受限的 Action 适配
// ✅ Edge OK：轻 CRUD
export const runtime = 'edge';
export async function createPost(data: PostInput) {
  const parsed = PostSchema.parse(data);
  return await db.posts.create(parsed);                  // HTTP driver < 5s
}
// ❌ Edge 限制：长操作
// export async function generateReport(id: string) {
//   const data = await db.largeQuery(id);               ← 可能 > 30s
//   const pdf = await generatePdf(data);                ← 需要 Node crypto
//   return pdf;                                          ← 可能 > 128MB
// }
// ✅ Edge OK：委派到队列（RBL-569）
export async function startReport(id: string) {
  const taskId = crypto.randomUUID();
  await queue.send({ taskId, type: 'report', id });      // 入队
  return { taskId };                                     // 立即返回
}
// Node runtime 的路由（重操作）
// app/api/report/route.ts
export const runtime = 'nodejs';                        // Node：fs/crypto 可用
```
