---
title: [BAS-055] data-* 属性和 dataset 有什么关系？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-055：data-* 属性和 dataset 有什么关系？
**答**：
- data-* 是 HTML 合法的自定义属性，用于在元素上挂业务数据，不影响渲染语义。
- JS 通过 dataset 读写：`data-user-id` 对应 `dataset.userId`，中划线自动转驼峰。
- CSS 可用属性选择器 `[data-state="open"]` 做状态样式，或 `content: attr(data-tip)` 读取值。

```html
<div id="card" data-user-id="42" data-state="open">卡片</div>
<script>
  const card = document.getElementById('card');
  console.log(card.dataset.userId);  // "42"，中划线转驼峰
  card.dataset.state = 'closed';     // 写回后即 data-state="closed"
</script>
```
