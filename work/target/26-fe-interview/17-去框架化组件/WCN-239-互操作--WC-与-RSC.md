---
title: [WCN-239] React Server Components 场景下自定义元素的边界与可行模式？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-239：React Server Components 场景下自定义元素的边界与可行模式？
**答**：
- RSC 输出是序列化的 UI 描述——自定义元素标签可以作为「叶子节点」出现在 RSC 输出（React 19 支持）。
- 限制：元素 props 必须可序列化（函数/复杂交互逻辑不能从 Server 传）。
- 交互逻辑：元素内部自治（自行 fetch 或由 Client Component 包装注入 property）。
- 模式：Server 渲染 DSD 静态骨架 + Client Component 包裹注水交互。

```javascript
// RSC：静态部分直接用元素（props 可序列化）
export default async function Page() {
  const goods = await db.getGoods();
  return <goods-card sku={goods.sku} title={goods.title} price={goods.price} />;
}
// 交互部分由 Client Component 包装（传事件回调/状态句柄）
r
```
