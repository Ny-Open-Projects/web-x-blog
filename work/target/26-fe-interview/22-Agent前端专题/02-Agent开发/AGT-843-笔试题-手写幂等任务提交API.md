---
title: [AGT-843] 手写 submitTask：Idempotency-Key 必选、重放返回原结果、进行中返回状态、存储层防并发写？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-843：手写 submitTask：Idempotency-Key 必选、重放返回原结果、进行中返回状态、存储层防并发写

**需求与边界**：
- 实现 submitTask(req)。
- 边界要求：① 无 Idempotency-Key 返回 400（文档约定必选）；② 重放：已完成返回原结果（200 + replayed 标记），进行中返回 202 + 任务状态，不重复创建；③ 并发同 key 双请求只创建一个（存储层唯一键）；④ key 与请求体哈希绑定（同 key 不同体返回 422）。

**答**：
```javascript
async function submitTask(req) {
  const key = req.headers['idempotency-key'];
  if (!key) return { status: 400,
    code: 'idempotency.required' };                // 必选
  const bodyHash = hash(JSON.stringify(req.body));
  const existing = await idem.get(key);
  if (existing) {
    if (existing.bodyHash !== bodyHash)
      return { status: 422,
        code: 'idempotency.mismatch' };            // key体不匹配
    if (existing.done)
      return { status: 200, ...existing.result, replayed: true };
    return { status: 202, taskId: existing.taskId,
      status: 'in-progress' };                     // 进行中
  }
  const created = await idem.putIfAbsent(key, {    // 原子占位
    bodyHash, taskId: null, done: false });
  if (!created) return submitTask(req);            // 并发抢失败重查
  const task = await runtime.dispatch(req.body);
  await idem.set(key, { bodyHash, taskId: task.id, done: false });
  return { status: 202, taskId: task.id };
}
```

**评分点**:
- key 必选+体哈希绑定（防同 key 不同语义）；重放区分完成/进行中。
- putIfAbsent 原子占位防并发双建。

