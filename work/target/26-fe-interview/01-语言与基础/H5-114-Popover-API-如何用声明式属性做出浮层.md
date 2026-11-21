---
title: [H5-114] Popover API 如何用声明式属性做出浮层？与 dialog 的分工？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-114：Popover API 如何用声明式属性做出浮层？与 dialog 的分工？
**答**：
- 三件套：`popover` 属性（auto/manual）标定浮层、`popovertarget` 属性绑定触发按钮、浏览器自动管理显示/隐藏与**顶层渲染**（无 z-index 战争、不裁剪于 overflow）。
- `auto` 模式自带"轻关闭"（light dismiss：点外部/Esc 关闭）与互斥（同开一个新 auto popover 会关旧的）；`manual` 不自动关闭，适合通知横幅。
- 事件：`beforetoggle/toggle`，`e.newState/e.oldState` 为 shown/hidden；样式用 `:popover-open` 匹配展开态，`@starting-style` 做入场过渡。
- 与 dialog 分工：popover 是**非模态**轻浮层（菜单、tooltip、选择器），不阻断页面交互；dialog `showModal()` 是模态（含焦点陷阱与 ::backdrop），表单确认类场景用它。
- 兼容：Chrome 114+、Safari 17+、Firefox 125+，主流可用；旧环境需 polyfill 或组件库。

```html
<!-- 声明式下拉菜单：零 JS -->
<button popovertarget="menu">更多操作</button>

<div id="menu" popover>
  <ul>
    <li><button>重命名</button></li>
    <li><button>移动到…</button></li>
    <li><button class="danger">删除</button></li>
  </ul>
</div>

<style>
  #menu {
    inset: auto;                            /* 覆盖默认全屏定位，交给 anchor 或手写 */
    margin: 0; padding: 4px;
    border: 1px solid #ddd; border-radius: 8px;
    box-shadow: 0 8px 24px #0002;
  }
  /* 入场过渡：starting-style 定义起始态 */
  #menu {
    opacity: 1; transform: translateY(0);
    transition: opacity .2s, transform .2s, display .2s allow-discrete;
  }
  @starting-style { #menu { opacity: 0; transform: translateY(-4px); } }
</style>

<script>
  const menu = document.getElementById('menu');
  // 状态事件：埋点或联动逻辑
  menu.addEventListener('toggle', (e) => {
    console.log(`popover ${e.oldState} -> ${e.newState}`);
  });
  // 程序化控制
  // menu.showPopover(); menu.hidePopover(); menu.togglePopover();
</script>
```
