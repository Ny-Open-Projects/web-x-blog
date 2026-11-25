---
title: [CSS-304] 笔试：纯 CSS 模态弹窗（dialog）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 组件]
type: 笔试题
---

## CSS-304：笔试：纯 CSS 模态弹窗

**题目**：用原生 dialog 实现模态弹窗：点击按钮打开（popovertarget 或少量 JS）、带遮罩毛玻璃、出入场动画、Esc 关闭、点击遮罩关闭（纯 CSS + 原生方法）。

**答**：
```css
dialog.modal {
  border: none; border-radius: 12px;
  padding: 0; max-width: 90vw;
  box-shadow: 0 8px 40px rgb(0 0 0 / .3);
}
dialog.modal::backdrop {
  background: rgb(0 0 0 / .5);
  backdrop-filter: blur(4px);
}
/* 出入场动画（overlay + display 可过渡） */
dialog.modal {
  opacity: 1; transform: none;
  transition: opacity .3s, transform .3s, overlay .3s allow-discrete, display .3s allow-discrete;
}
dialog.modal:not([open]) { opacity: 0; transform: translateY(16px); }
@starting-style {
  dialog.modal[open] { opacity: 0; transform: translateY(16px); }
}
dialog.modal::backdrop {
  transition: opacity .3s, overlay .3s allow-discrete;
}
```
```html
<button onclick="d.showModal()">打开</button>
<dialog id="d" class="modal" onclick="if (event.target === this) this.close()">
  <div style="padding:24px">
    <h3>确认操作</h3>
    <form method="dialog"><button value="ok">确定</button></form>
  </div>
</dialog>
```

**评分点**：
- showModal 进 top layer（z-index 无关、自动焦点、Esc 原生关闭）
- 点击遮罩关闭的 target 判断（或 CSS-only 的 :target 方案对比）
- overlay allow-discrete 让离场动画播完再移除
- ::backdrop 毛玻璃与动画
