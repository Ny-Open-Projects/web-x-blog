---
title: [H5-115] dialog 元素与 ::backdrop 的正确用法与坑。
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-115：dialog 元素与 ::backdrop 的正确用法与坑。
**答**：
- 三种打开方式语义不同：`show()` 非模态（仍在文档流、无遮罩）、`showModal()` 模态（进入 top layer、自动 ::backdrop、焦点陷阱、Esc 触发 cancel 可关闭）。
- 关闭：`close(returnValue)` 携带返回值；表单 `method="dialog"` 提交即关闭并写入 returnValue，是最优雅的确认框模式。
- 样式：`dialog::backdrop` 做遮罩；`dialog[open]` 控制展开态；入场动画用 `@starting-style` + transition（display 不可动画需 `allow-discrete`）。
- 焦点管理自动完成：打开时聚焦第一个可聚焦元素或 `autofocus` 元素；关闭后焦点归还触发者（现代浏览器已内置）。
- 坑：`showModal()` 要求 dialog 在文档中；`cancel` 事件不 `preventDefault()` 则 Esc 直接关；关闭动画需要监听 `animationend` 延迟移除 open。

```html
<button id="open">打开确认框</button>

<dialog id="confirm-dialog">
  <form method="dialog">                       <!-- 提交即关闭 -->
    <p>确认删除该文件？</p>
    <menu>
      <button value="cancel" formnovalidate>取消</button>
      <button value="confirm" autofocus>确认删除</button>
    </menu>
  </form>
</dialog>

<style>
  dialog {
    border: none; border-radius: 12px;
    padding: 24px 32px;
    box-shadow: 0 12px 40px #0003;
  }
  /* 遮罩：只能作用于 ::backdrop，写在 dialog 上无效 */
  dialog::backdrop {
    background: #0009;
    backdrop-filter: blur(2px);
  }
  /* 入场动画 */
  dialog[open] { animation: pop .25s ease-out; }
  @keyframes pop {
    from { opacity: 0; transform: translateY(12px) scale(.96); }
  }
</style>

<script>
  const dlg = document.getElementById('confirm-dialog');
  document.getElementById('open').addEventListener('click', () => dlg.showModal());

  // Esc / 关闭按钮都会走 close，returnValue 区分结果
  dlg.addEventListener('close', () => {
    const result = dlg.returnValue;            // "confirm" | "cancel"
    console.log('用户选择：', result);
    if (result === 'confirm') doDelete();
  });

  // 拦截 Esc：确认框要求显式选择时
  dlg.addEventListener('cancel', (e) => e.preventDefault());
</script>
```
