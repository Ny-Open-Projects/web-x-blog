---
title: [PER-977] 布局树构建的深水点：display:contents 与匿名盒的影响
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-977：布局树构建的深水点：display:contents 与匿名盒的影响

**答**：
- display:contents 让元素自身不生成盒，子元素直接参与父级布局——可减少包裹层，但删除元素盒也删除了它的可访问性语义（旧版浏览器）。
- 匿名盒：文本混排生成的匿名块盒增加布局复杂度，深度嵌套 + 行内块混排让 Layout 变慢。
- 实践：用 contents 减少无样式包装 div 时，确认子元素布局上下文不变；a11y 属性转移到子元素。
- 度量：Layout 时长 + 布局树规模（DevTools Layers/内存面板），深嵌套列表页收益明显。

```javascript
<div class="grid" style="display:contents">
  <!-- wrapper 不生成盒，children 直接成为 grid items -->
  <div class="cell">A</div><div class="cell">B</div>
</div>
<script>
// contents 前后的布局对比实验
function benchLayout(el, n = 50) {
  const t0 = performance.now();
  for (let i = 0; i < n; i++) {
    el.style.width = (100 + i) + 'px';
    void el.offsetHeight;                 // 强制布局
  }
  return +(performance.now() - t0).toFixed(1);  // ms，越小越好
}
</script>
```
