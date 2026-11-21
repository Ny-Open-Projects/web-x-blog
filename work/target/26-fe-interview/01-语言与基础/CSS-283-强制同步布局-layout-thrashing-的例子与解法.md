---
title: [CSS-283] 强制同步布局：layout thrashing 的例子与解法
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## CSS-283：强制同步布局的例子与解法

**答**：
- 机制：读取布局属性（offsetWidth/getBoundingClientRect）时，若样式已脏，浏览器被迫立即同步 layout——同一帧内多次「读-写-读」形成抖动循环
- 经典反例：for 循环里读 offsetTop 再写 style.top（无限触发 layout）
- 解法一：FastDOM 类库自动批量读写；解法二：手动分离——先收集全部读值，再统一写；解法三：避免读布局，用 IntersectionObserver/ResizeObserver 替代
- rAF 的作用：把写操作挪到下一帧，读写天然分离
- 检测：Performance 面板紫色 Layout 条块密集出现 + "Forced reflow" 提示

```javascript
// 反例
items.forEach(el => el.style.height = el.scrollHeight + 10 + 'px'); // 每次读都强制布局
// 正例
const heights = items.map(el => el.scrollHeight);      // 集中读
items.forEach((el, i) => (el.style.height = heights[i] + 10 + 'px')); // 集中写
```
