---
title: [V3-280] 弹窗嵌套与 z-index 层级管理方案是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-280：弹窗嵌套与 z-index 层级管理方案是什么？
**答**：
- 层级问题根源：弹窗经 Teleport 到 body 后脱离原 stacking context，固定 z-index 写死会在嵌套弹窗/Toast 冲突时出错。
- 方案：全局**层级栈管理器**——每打开一个浮层 push 到栈顶并分配递增 z-index（基准 2000 起），关闭时 pop；同层级类型间有偏移段（dialog 2000+ / drawer 3000+ / toast 4000+）。
- 焦点管理：打开时记录 triggerElement，关闭后 `focus()` 还原；栈顶浮层才可 Tab 循环（aria-modal + inert 其余内容）。
- Esc 关闭只作用于栈顶；遮罩点击是否关闭由每层配置决定（确认类弹窗防误触禁用遮罩关闭）。
- 与 Provide/Inject 结合：弹窗服务 `useDialog()` 经 app.provide 全局可用，组件内部无需各自 Teleport。

```typescript
// 层级栈管理器
const stack: { id: symbol; z: number }[] = [];
let base = 2000;
function openLayer() {
  const z = base + stack.length * 10;              // 栈顶递增
  const entry = { id: Symbol('layer'), z };
  stack.push(entry);
  return { z, close: () => closeLayer(entry) };
}
function closeLayer(entry) {
  const i = stack.indexOf(entry);
  if (i > -1) stack.splice(i, 1);
}
function topLayer() { return stack[stack.length - 1]; }
// Esc：全局监听只关栈顶
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') topLayer()?.onEsc?.();
});
// useDialog 服务
export function useDialog() {
  return { confirm: (opts) => openDialog({ ...opts, ...openLayer() }) };
}
```
