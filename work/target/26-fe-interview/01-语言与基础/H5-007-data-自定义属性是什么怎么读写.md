---
title: [H5-007] data-* 自定义属性是什么？怎么读写？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-007：data-* 自定义属性是什么？怎么读写？
**答**：
- 以 `data-` 开头的特性用于在元素上挂自定义数据，HTML 合法且不污染全局。
- JS 通过 `el.dataset` 读写，驼峰对应连字符（`data-user-id` ↔ `dataset.userId`）；值都是字符串。
- CSS 可以用 `attr()` 读取，配合选择器 `[data-state="open"]` 实现状态驱动样式。
- 注意 dataset 是字符串，数字与布尔要自己转换；大量结构化数据建议放 JS 状态而非 DOM。

```html
<!-- 用 data-* 存业务数据，CSS 按状态渲染 -->
<div class="toast" data-type="success" data-auto-close="3000">保存成功</div>

<style>
  .toast[data-type='success'] { border-color: #34c759; }
  .toast[data-type='error']   { border-color: #ff3b30; }

  /* CSS 也能读取 data-* 内容 */
  .badge::after { content: attr(data-count); }
</style>

<script>
  const toast = document.querySelector('.toast');
  console.log(toast.dataset.type);       // "success"
  console.log(toast.dataset.autoClose);  // "3000"（字符串！）
  const delay = Number(toast.dataset.autoClose); // 需手动转数字

  toast.dataset.type = 'error';   // 写入会同步反映到 HTML 特性
  toast.dataset.userId = '42';    // HTML 中呈现为 data-user-id="42"
</script>
```
