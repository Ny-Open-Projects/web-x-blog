---
title: [WCN-975] SSR→hydration 切换时键盘焦点怎么保持：服务端 tabindex 与客户端重建对齐
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-975：SSR→hydration 切换时键盘焦点怎么保持：服务端 tabindex 与客户端重建对齐

**答**：
- 结论先行：焦点丢失是 SSR 水合的高发 a11y bug——hydration 若替换 DOM 节点，正在聚焦的元素被卸载，焦点掉到 body，键盘用户被迫从头 Tab。
- 对齐原则：hydration 复用 SSR DOM（不整体替换），只绑定事件与补状态，原生 tabindex/focus 语义保持不变。
- 必须重建的场景：先记录 `document.activeElement` 的标识（data-focus-id），重建后按标识 restore focus；无法复用焦点时用 `aria-activedescendant` 指向等效节点。
- WC 影子树焦点：用 delegatesFocus + shadow root 内 tabindex 管理，hydration 不重建 shadow 树结构；动态列表重渲染后按 key 恢复焦点（前文焦点恢复可复用）。
- 追问钩子：面试官问「SSR HTML 里该不该写 autofocus」——答：谨慎，autofocus 在 SSR 首屏会抢焦点且读屏器可能未就绪，通常交给 hydration 后按用户意图聚焦。

```javascript
// hydration 前后焦点保持
const active = document.activeElement;
const focusId = active && active.dataset ? active.dataset.focusId : null;
rehydrateDom(); // 可能重建
if (focusId) {
  const next = document.querySelector(`[data-focus-id="${focusId}"]`);
  next && next.focus(); // 按标识恢复焦点
}
// 优先：hydration 只 patch 不替换，焦点天然保留
function patchNode(old, next) {
  old.textContent = next.textContent; // 复用节点
  return old;
}
```
