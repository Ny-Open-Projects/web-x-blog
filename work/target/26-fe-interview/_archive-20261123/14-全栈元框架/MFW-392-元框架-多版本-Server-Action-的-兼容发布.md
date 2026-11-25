---
title: [392] 灰度期间新旧版本的 Server Action 如何做协议兼容
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, Server Action, 灰度发布]
type: 面试题
---

## MFW-392：灰度期间新旧版本的 Server Action 如何做协议兼容？

**答**：
- Server Action 的调用端是旧 HTML 里埋好的序列化 ID，端上拿着 ID 调服务端：灰度期新版必须保留旧 Action 的 ID 映射，否则老用户提交直接 404。
- 参数走「只增不改」：新字段可选、旧字段保留，服务端按入参版本分派到不同实现函数，响应结构对旧端维持原样。
- Action 的幂等与重放：灰度切换瞬间同一请求可能落到任一版本，写操作必须带 Idempotency-Key，两版本共享同一去重存储。
- 发布节奏：先双跑（新 Action 只写影子数据对比）-> 切流 -> 观察期后删旧实现，删除前用调用监控确认旧 ID 归零。

```ts
'use server';
// 旧版 actionId: a1 -> submitOrderV1；新版保留同一入口分派
const impls: Record<string, (p: any) => Promise<Rsp>> = {
  v1: submitOrderV1, v2: submitOrderV2,
};
export async function submitOrder(payload: { ver?: 'v1'|'v2'; idemKey: string; ... }) {
  if (await idem.has(payload.idemKey)) return idem.get(payload.idemKey); // 双版本共享去重
  const run = impls[payload.ver ?? 'v1'];   // 未带版本的老客户端走 v1
  const rsp = await run(payload);
  await idem.set(payload.idemKey, rsp, 60 * 10);
  return rsp;
}
async function submitOrderV2(p: any) { ... } // 只增字段，v1 语义不变
```
