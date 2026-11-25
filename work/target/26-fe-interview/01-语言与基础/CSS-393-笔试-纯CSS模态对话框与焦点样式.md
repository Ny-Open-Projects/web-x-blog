---
title: [CSS-393] 笔试：手写模态对话框（样式 + 无障碍要点）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## CSS-393：笔试：手写模态对话框（样式 + 无障碍要点）

**答**：实现模态：① 遮罩 + 居中弹窗，出现/消失动画（缩放+淡入，用 dialog 元素原生能力）；② 弹窗内容超高内部滚动、遮罩点击关闭、ESC 关闭；③ 滚动锁定（打开时 body 不滚且不跳动）；④ 无障碍：dialog 原生焦点管理 + ::backdrop。给出 HTML/CSS 与最小 JS。

```html
<dialog id="dlg">
  <form method="dialog">
    <h2>确认操作</h2>
    <div class="body">内容可滚动...</div>
    <button value="ok">确定</button>
  </form>
</dialog>
```

```css
dialog {
  border: none; border-radius: 12px;
  padding: 0; width: min(480px, 90vw);
  animation: pop .25s var(--ease-out-quart);
}
dialog::backdrop { background: rgb(0 0 0 / .45); animation: fade .25s; }
dialog .body { max-height: 60dvh; overflow: auto; }
@keyframes pop { from { transform: scale(.95); opacity: 0; } }
@keyframes fade { from { opacity: 0; } }

body.modal-open { overflow: hidden; }  /* 配合 scrollbar-gutter 防跳动 */
html { scrollbar-gutter: stable; }
```

```javascript
const dlg = document.getElementById('dlg');
function openModal() {
  document.body.classList.add('modal-open');
  dlg.showModal();                          // 原生: 焦点困住 + ESC 关闭
}
dlg.addEventListener('close', () => document.body.classList.remove('modal-open'));
dlg.addEventListener('click', (e) => {
  if (e.target === dlg) dlg.close();        // 点击遮罩关闭
});
```

**评分点**：
- `<dialog>` 原生能力（showModal 焦点陷阱 + ESC + ::backdrop）
- 滚动锁定 + scrollbar-gutter 防布局跳动
- 遮罩点击判定用 e.target === dialog
- 进出场动画与无障碍语义完整
