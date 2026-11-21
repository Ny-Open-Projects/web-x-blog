---
title: [R19-066] 如何实现一个完整的 Portal 弹窗组件？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-066：如何实现一个完整的 Portal 弹窗组件？
**答**：
- createPortal 挂到 document.body，天然摆脱父级 overflow 和 z-index 层叠上下文限制。
- 焦点管理三步：打开时聚焦弹窗内第一个可聚焦元素、Tab 循环圈定在弹窗内、关闭后归还焦点给触发元素。
- Esc 关闭、点击遮罩关闭、body 滚动锁定，都在同一个 effect 中注册与清理。
- 无障碍用 role="dialog" + aria-modal="true" + aria-label。

```jsx
import { useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';

export function Modal({ open, onClose, title, children }) {
  const dialogRef = useRef(null);
  const lastActiveRef = useRef(null);

  useEffect(() => {
    if (!open) return;
    lastActiveRef.current = document.activeElement;
    const dialog = dialogRef.current;
    dialog?.querySelector('button, [href], input')?.focus();

    const onKeyDown = (e) => {
      if (e.key === 'Escape') onClose?.();
      if (e.key === 'Tab') {
        // 焦点圈定在弹窗内循环
        const focusables = dialog.querySelectorAll('button, [href], input, textarea, [tabindex]:not([tabindex="-1"])');
        const first = focusables[0];
        const last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
        else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
      }
    };
    document.addEventListener('keydown', onKeyDown);
    document.body.style.overflow = 'hidden';
    return () => {
      document.removeEventListener('keydown', onKeyDown);
      document.body.style.overflow = '';
      lastActiveRef.current?.focus?.();   // 关闭后归还焦点
    };
  }, [open, onClose]);

  if (!open) return null;
  return createPortal(
    <div className="modal-mask" onMouseDown={e => e.target === e.currentTarget && onClose?.()}>
      <div role="dialog" aria-modal="true" aria-label={title} ref={dialogRef}>
        <header>{title}</header>
        {children}
      </div>
    </div>,
    document.body,
  );
}
```
