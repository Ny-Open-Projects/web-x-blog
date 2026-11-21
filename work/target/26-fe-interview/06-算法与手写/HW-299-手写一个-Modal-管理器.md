---
title: [HW-299] 手写一个 Modal 管理器：多弹窗栈、焦点陷阱与层级管理
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-299：手写一个 Modal 管理器：多弹窗栈、焦点陷阱与层级管理

**答**：
- 需求：实现 ModalManager：open(component, opts) 压栈（同一时刻可多个 modal）；z-index 递增分配；Esc 关闭栈顶；焦点陷阱（Tab 循环在 modal 内，打开时聚焦第一个可聚焦元素，关闭后归还焦点给触发者）；body 滚动锁定按栈深管理。
- 边界：栈顶才响应 Esc；焦点陷阱查可聚焦元素（button/input/[tabindex]）；最后一个 modal 关闭才解锁 body 滚动。
- 评分点：栈结构；焦点归还；滚动锁计数。

```javascript
class ModalManager {
  constructor() { this.stack = []; this.z = 1000; this.scrollLocks = 0; }
  open(render, { onClose } = {}) {
    const el = render();
    const z = ++this.z;
    el.style.zIndex = z;
    const trigger = document.activeElement;                  // 记录触发者
    const entry = { el, z, onClose, trigger,
      handler: e => { if (e.key === 'Escape') this.close(entry); } };
    document.addEventListener('keydown', entry.handler);
    document.body.appendChild(el);
    this.stack.push(entry);
    if (++this.scrollLocks === 1) document.body.style.overflow = 'hidden';   // 滚动锁计数
    requestAnimationFrame(() => {
      const focusable = el.querySelectorAll('button,input,[tabindex]:not([tabindex="-1"])');
      focusable[0]?.focus();                                 // 聚焦第一个可聚焦
    });
    el.addEventListener('keydown', e => this.trapTab(e, el));
    return entry;
  }
  trapTab(e, el) {                                           // Tab 循环陷阱
    if (e.key !== 'Tab') return;
    const f = [...el.querySelectorAll('button,input,[tabindex]:not([tabindex="-1"])')]
      .filter(x => !x.disabled);
    if (!f.length) return;
    const first = f[0], last = f.at(-1);
    if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
    else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
  }
  close(entry) {
    const i = this.stack.indexOf(entry);
    if (i < 0 || i !== this.stack.length - 1) return false;  // 只关栈顶
    document.removeEventListener('keydown', entry.handler);
    entry.el.remove();
    entry.trigger?.focus?.();                                // 焦点归还
    this.stack.pop();
    if (--this.scrollLocks === 0) document.body.style.overflow = '';
    entry.onClose?.();
    return true;
  }
}
```
