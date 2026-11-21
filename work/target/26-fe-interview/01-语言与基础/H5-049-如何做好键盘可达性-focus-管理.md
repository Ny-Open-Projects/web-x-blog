---
title: [H5-049] 如何做好键盘可达性（focus 管理）？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-049：如何做好键盘可达性（focus 管理）？
**答**：
- 默认规则：所有交互用原生控件（button/a/input），天然支持 Tab、Enter、空格与焦点样式。
- 自定义弹窗三板斧：打开时焦点移入弹窗、Tab 循环困在弹窗内（focus trap）、关闭时焦点还给触发按钮。
- `tabindex`：-1 可编程聚焦但不进 Tab 序列；0 进入序列；正数打乱顺序，禁用。
- 不要用 `outline: none` 抹掉焦点样式；要美化用 `:focus-visible`。

```javascript
// 弹窗的焦点管理：打开移入 + 关闭归还 + Tab 困住
class Dialog {
  constructor(el) {
    this.el = el;
    this.lastFocused = null;

    el.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') this.close();

      if (e.key === 'Tab') {
        const focusables = el.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
        const first = focusables[0];
        const last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus(); // 反向到头，绕回最后一个
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus(); // 正向到头，绕回第一个
        }
      }
    });
  }

  open() {
    this.lastFocused = document.activeElement;
    this.el.hidden = false;
    this.el.querySelector('h2')?.focus(); // 标题设 tabindex="-1" 作为初始焦点
  }

  close() {
    this.el.hidden = true;
    this.lastFocused?.focus(); // 焦点还给触发按钮，键盘用户不迷路
  }
}
```

```html
<div class="dialog" role="dialog" aria-modal="true" aria-labelledby="dlg-title" hidden>
  <h2 id="dlg-title" tabindex="-1">确认删除</h2>
  <button class="cancel">取消</button>
  <button class="confirm">删除</button>
</div>

<style>
  /* 保留焦点可见性：只对键盘操作显示焦点环 */
  button:focus-visible {
    outline: 2px solid #3367d6;
    outline-offset: 2px;
  }
  /* 反例：outline: none 会干掉所有键盘用户的导航线索 */
</style>
```
