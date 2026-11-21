---
title: [R19-095] 如何实现 Toast 与 Dialog 的命令式管理器？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-095：如何实现 Toast 与 Dialog 的命令式管理器？
**答**：
- 目标是业务侧一行调用：`toast.success('已保存')`、`await confirmDialog({...})`，不在组件树里手工摆状态。
- 实现方式：模块级维护 toasts 数组 + createRoot 挂载一次性宿主容器，每次增删全量重渲宿主。
- Dialog Promise 化：弹窗回调里 resolve，调用方用 await 写同步风格逻辑，消灭回调嵌套。
- 注意 React 18+ 的 createRoot 要复用同一个 root 实例，unmount 时统一清理。

```jsx
// toast.tsx —— 命令式 Toast 与 Promise 化 Dialog
import { createRoot } from 'react-dom/client';

function ToastApp({ toasts }) {
  return (
    <div className="overlay-host">
      {toasts.map(t =>
        t.type === 'dialog'
          ? <Dialog key={String(t.id)} {...t} />   // Dialog 内部点击调用 t.onOk / t.onCancel
          : <div key={t.id} className={`toast toast-${t.type}`}>{t.content}</div>,
      )}
    </div>
  );
}

let root = null;
let toasts = [];

function ensureRoot() {
  if (root) return;
  const container = document.createElement('div');
  document.body.appendChild(container);
  root = createRoot(container);
}

function renderAll() { root.render(<ToastApp toasts={toasts} />); }

function push(item, duration) {
  ensureRoot();
  toasts = [...toasts, item];
  renderAll();
  if (duration) {
    setTimeout(() => {
      toasts = toasts.filter(t => t.id !== item.id);
      renderAll();
    }, duration);
  }
}

export const toast = {
  show: (content, options = {}) => push({ id: Date.now(), content, duration: 3000, ...options }, options.duration),
  success: (content) => toast.show(content, { type: 'success' }),
  error: (content) => toast.show(content, { type: 'error' }),
};

// Promise 化 confirm：调用即弹窗，await 拿结果
export function confirmDialog({ title, content }) {
  return new Promise(resolve => {
    ensureRoot();
    const dialogId = Symbol('dialog');
    const close = (result) => {
      toasts = toasts.filter(t => t.id !== dialogId);
      renderAll();
      resolve(result);
    };
    toasts = [...toasts, {
      id: dialogId, type: 'dialog', title, content,
      onOk: () => close(true),
      onCancel: () => close(false),
    }];
    renderAll();
  });
}

// 调用方：
// const ok = await confirmDialog({ title: '删除', content: '确认删除该条记录？' });
// if (ok) await removeItem(id);
```

---

## 第十五章 性能实战（R19-096 ~ R19-101）
