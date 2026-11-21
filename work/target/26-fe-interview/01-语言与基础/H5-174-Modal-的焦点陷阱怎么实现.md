---
title: [H5-174] Modal 的焦点陷阱怎么实现？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-174：Modal 的焦点陷阱怎么实现？
**答**：
- 打开时记住 `document.activeElement`，焦点移入 modal（首个可聚焦元素或 `tabindex=-1` 的标题）；关闭后焦点归还触发元素——焦点不归还是最高频的无障碍缺陷。
- Tab 循环：keydown 捕获 Tab，收集容器内可见可聚焦元素，正向往尾则跳头、Shift+Tab 向头则跳尾。
- 屏蔽外部：给背景元素设置 `inert`（整树不可聚焦不可点击，强于 aria-hidden）；`<dialog>.showModal()` 原生自带焦点陷阱 + Esc，优先用原生。
- 配套：`role="dialog" aria-modal="true" aria-labelledby` 指向标题；Esc 关闭；动态内容变化时焦点不丢失。

```javascript
class Modal {
  static FOCUSABLE =
    'a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])';
  #lastActive = null;
  constructor(dialog) { this.dialog = dialog; }

  open() {
    this.#lastActive = document.activeElement;      // 记住触发者
    this.dialog.hidden = false;
    // 屏蔽外部交互：inert 让背景整树不可聚焦不可点击（强于 aria-hidden）
    for (const el of document.body.children)
      if (el !== this.dialog.parentElement) el.inert = true;
    // 焦点落标题（tabindex=-1 可聚焦但不进 Tab 链）或第一个控件
    (this.dialog.querySelector('[autofocus]') ??
     this.dialog.querySelector('h2')).focus();
    this.#bind();
  }
  close() {
    this.dialog.hidden = true;
    for (const el of document.body.children) el.inert = false;
    this.#lastActive?.focus();                      // 焦点归还触发者
  }
  #bind() {
    this.dialog.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') return this.close();
      if (e.key !== 'Tab') return;
      const items = [...this.dialog.querySelectorAll(Modal.FOCUSABLE)]
        .filter((el) => el.offsetParent !== null);   // 排除隐藏元素
      if (!items.length) return e.preventDefault();
      const first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) {
        last.focus(); e.preventDefault();            // 反向到头 → 回到最后
      } else if (!e.shiftKey && document.activeElement === last) {
        first.focus(); e.preventDefault();           // 正向到头 → 回到第一个
      }
    });
  }
}
// 配套 HTML：role="dialog" aria-modal="true" aria-labelledby="dlg-title"
// 原生替代：<dialog>.showModal() 自带焦点陷阱 + Esc + inert 效果，优先用原生
```
