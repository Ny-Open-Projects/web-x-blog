---
title: [CSS-262] dialog 元素的样式体系：::backdrop 与 open
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 组件]
type: 面试题
---

## CSS-262：dialog 元素的样式体系：::backdrop 与 open

**答**：
- dialog 原生模态：showModal() 进 top layer（z-index 无关）、自动焦点管理、Esc 关闭、::backdrop 遮罩
- 样式要点：dialog 默认白底黑框有 margin:auto 居中——重置后自定义；::backdrop 只能改背景/滤镜/模糊
- 状态选择：dialog[open] 控制打开态样式；关闭态默认 display:none
- 与 backdrop-filter：遮罩毛玻璃 `::backdrop { backdrop-filter: blur(4px) }` 现代浏览器可用
- 表单方法：`method="dialog"` 的 form 提交直接关弹窗，returnValue 拿返回值——无 JS 交互闭环

```css
dialog {
  border: none; border-radius: 12px;
  padding: 24px; max-width: 90vw;
  box-shadow: 0 8px 40px rgb(0 0 0 / .3);
}
dialog::backdrop { background: rgb(0 0 0 / .5); backdrop-filter: blur(4px); }
```
```html
<dialog id="d" method="dialog"><p>确定删除？</p><button value="ok">确定</button></dialog>
```
