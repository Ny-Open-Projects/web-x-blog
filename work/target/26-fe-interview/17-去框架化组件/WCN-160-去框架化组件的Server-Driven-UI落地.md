---
title: [WCN-160] 去框架化组件在 Server-Driven UI 中的落地：服务端下发组件树怎么消费？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-160：去框架化组件在 Server-Driven UI 中的落地：服务端下发组件树怎么消费？

**答**：
- 模式：服务端下发 UI 描述（`{ tag, attrs, children, events }` 树），客户端渲染器还原为 WC 树；动态化运营位、A/B 实验无需发版。
- 与 WC 的契合：WC 的 tag 是"平台无关字符串"，客户端只需 `createElement(tag) + setAttribute`，无需框架组件注册表——这是 SDUI 选 WC 的核心理由。
- 安全约束：tag 白名单（registry 校验）、attribute 值类型校验、事件绑定走声明式（`on:tap → 客户端 handler 映射表`），禁止服务端下发任意 JS。
- 懒加载：树里出现的 tag 未 define → 触发加载器（WCN-044 调度器）；渲染前等待 `whenDefined` 或先骨架。
- 状态与会话：SDUI 树是无状态的，交互产生的状态回流（如表单提交）走数据接口而非重新拉树；树更新用 patch（按 node id diff）而不是整树重建。

```javascript
// SDUI 渲染器（核心 20 行）
const REGISTRY = new Set(['acme-banner', 'acme-button', 'acme-list']);
function renderNode(n) {
  if (!REGISTRY.has(n.tag)) throw new Error(`非法组件: ${n.tag}`);   // 白名单
  const el = document.createElement(n.tag);
  for (const [k, v] of Object.entries(n.attrs ?? {})) el.setAttribute(k, String(v));
  for (const child of n.children ?? []) el.append(typeof child === 'string' ? child : renderNode(child));
  return el;
}
async function mount(tree, container) {
  await Promise.all(collectTags(tree).map((t) => customElements.whenDefined(t))); // 等待 define
  container.replaceChildren(renderNode(tree));
}
```
