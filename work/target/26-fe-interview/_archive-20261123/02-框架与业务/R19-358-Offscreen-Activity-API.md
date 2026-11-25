---
title: [R19-358] Offscreen（Activity API）：隐藏渲染与状态保留
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Suspense]
type: 面试题
---

## R19-358：Offscreen（Activity API）：隐藏渲染与状态保留

**答**：
- Activity API（原 Offscreen，React 19 正式名）：`<Activity mode="hidden">`——隐藏时不卸载组件，状态保留、DOM 移除、副作用暂停（effects 挂起）
- 与 display:none 手写的差异：hidden 模式下 effect 不执行（包括 useEffect 依赖的轮询/订阅暂停）——手动 display:none 不停 effect，浪费资源
- 双模式：hidden（卸 DOM 留状态）/visible——「预渲染」（mode 从 hidden 切 visible 即时显示）是性能武器：提前在隐藏树里渲染下一页
- 与 KeepAlive 对应：React 生态的 KeepAlive 需求终于有官方原语——tab 页切换、向导分步等场景
- 边界：hidden 时 cleanup 不执行、mount 也不执行——effect 首次执行推迟到 visible；这改变了「挂载即请求」的模型

```jsx
<Activity mode={activeTab === 'logs' ? 'visible' : 'hidden'}>
  <LogsPanel />   {/* 隐藏: 状态保留, effect 暂停, DOM 移除 */}
</Activity>
```
