---
title: [MFW-552] 元框架的 HMR 协议：模块图传播与组件状态保持
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-552：元框架 HMR 协议：模块图传播与状态保持

**答**:
- 元框架 HMR 的分层传播：1) **RSC 层**（server 文件变更 → re-render 受影响段 → Flight patch 推送——server 端失效传播 RBL-635；client 收到 patch 原位更新（Router Cache 更新 RBL-511））；2) **client 层**（client 组件变更 → Vite/Turbopack HMR——React Fast Refresh 状态保持）；3) **双层的协调**（page.tsx 变更 → server 重渲染 + client Fast Refresh——两层同时动）。
- Fast Refresh 的边界：保留 state 的条件（组件签名不变/无渲染期副作用——class 组件退化为整页刷新；hook 顺序变化 state 重置）。
- Server 组件变更的状态语义：RSC patch = server 数据更新（client 组件 props 变化 → re-render——client state 保留吗？——React 的 reconciliation：同位置同 key 保留 state）；「server 数据变了 client 表单还在」的期望由 reconciliation 保证。
- 追问钩子：为什么「RSC patch 到达」能保 client state 而「整页刷新」不能？——patch 是「同组件树的增量更新」（React 的 reconciliation 语义：同位置组件复用实例 → state 保留）；刷新 = DOM 全重建（state 消失）；「state 的存活 = React 实例的存活」——HMR 的状态保持本质是「diff 的粒度」：patch 粒度越细、state 存活越稳（RBL-600 accept 边界的框架版）。

```javascript
// RSC HMR patch 的推送（dev server 概念）
// server: 检测文件变更 → 最小失效集（RBL-635）→ 重新渲染受影响段
const { retransform } = invalidate({ changed: 'app/products/page.tsx', ... });
const flight = await renderToFlight(changedRoutes);
ws.send(JSON.stringify({ type: 'rsc-patch', flight }));  // 推送给 client
// client: 收到 patch → Router Cache 原位更新（RBL-511）
onRscPatch = (flight) => {
  routerCache.update(flight);                            // 不刷新页面
  // client 组件的 state 保留：React reconciliation 同位置复用
};
// Fast Refresh 边界（client 组件）
'use client';
export default function Editor({ initial }) {
  const [text, setText] = useState(initial);             // 签名不变 → state 保持
  // 反模式：渲染期副作用 → Fast Refresh 重执行 → 副作用重复
  // useEffect(() => {...}) 内做副作用：HMR 安全
}
```
