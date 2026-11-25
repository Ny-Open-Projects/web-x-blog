---
title: [MFW-801] RSC 渲染阶段为什么不能执行 Server Action，mutation 必须落在独立 POST
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-801：RSC 渲染阶段为什么不能执行 Server Action，mutation 必须落在独立 POST

**答**：
- 结论：Server Action 本质是独立的 POST RPC，只能在事件/表单提交触发的专属请求里运行，绝不能在渲染阶段（GET）调用——渲染必须纯读、可重放、可缓存。
- 原因：渲染会被预取、重试、流式分块甚至取消，在其中写库 = 副作用不可控（重复扣款、写入被 CDN 缓存进 HTML）；框架对渲染期调用 action 直接报错或生成不可靠引用。
- 追问钩子：首屏既要实时数据又要提交按钮怎么组织？——数据走 RSC 读、提交走 action POST，两者用 revalidateTag 衔接，而不是在 RSC 里直接写。

```javascript
// ❌ 错误：在 Server Component 渲染期间做写操作
async function ProductPage({ id }) {
  await db.stock.decrement(id);            // 渲染会被预取/重试 → 危险！
  const p = await db.product.find(id);
  return <Buy product={p} />;
}

// ✅ 正确：渲染只读；mutation 交给独立 Server Action（POST）
async function ProductPage({ id }) {
  const p = await db.product.find(id);     // 纯读，可缓存/去重
  return <Buy product={p} onBuy={buyAction} />;
}

async function buyAction(formData) {
  'use server';                            // 编译成稳定 id 的 POST 端点
  const sku = formData.get('sku');
  await db.order.create({ sku });          // 写只发生在 action 里
  revalidateTag('stock-' + sku);           // 失效读缓存 → 触发 RSC 重渲染
}

// 框架视角：POST /?_rsc=...  body: $ACTION_ID_<hash>&sku=...
// 渲染 GET 永远不携带 action id —— 渲染与 mutation 物理隔离
```
