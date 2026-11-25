---
title: [CSS-397] 笔试：手写手风琴（details 原生方案 + 高度动画）
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 笔试题, 交互]
type: 笔试题
---

## CSS-397：笔试：手写手风琴（details 原生方案 + 高度动画）

**答**：实现 FAQ 手风琴：① 用原生 details/summary（自带键盘与无障碍）；② 展开/收起高度动画（details 原生不支持动画，用 interpolate-size 或 grid-rows 技巧）；③ 同时只展开一项（互斥）；④ 箭头旋转指示；⑤ 老内核降级（瞬时展开）。写出核心实现。

```html
<details name="faq" open>
  <summary>如何退款? <i class="arrow"></i></summary>
  <div class="body">申请后 1-3 个工作日到账...</div>
</details>
```

```css
details {
  border-bottom: 1px solid #eee;
}
details .body {
  overflow: hidden;
  max-height: 0;
  transition: max-height .3s var(--ease-out-quart),
              opacity .3s;
  opacity: 0;
}
details[open] .body {
  max-height: 300px;              /* 预估上限, 内容少时有过渡空窗 */
  opacity: 1;
}
/* 现代 Chrome 129+: interpolate-size 支持真实高度动画 */
@supports (interpolate-size: allow-keywords) {
  details .body { max-height: 0; transition: height .3s; height: 0; }
  details[open] .body { height: auto; }
}
summary { list-style: none; cursor: pointer; }
summary::-webkit-details-marker { display: none; }
.arrow { transition: transform .3s; display: inline-block; }
details[open] .arrow { transform: rotate(90deg); }
```

```javascript
// 互斥: name 属性已原生支持(Clash) —— 老内核 JS 兜底
document.querySelectorAll('details[name=faq]').forEach(d =>
  d.addEventListener('toggle', () => {
    if (d.open) document.querySelectorAll('details[name=faq]')
      .forEach(o => { if (o !== d) o.open = false; });
  }));
```

**评分点**：
- details/summary 原生无障碍（回车/空格展开）
- max-height 过渡的空窗缺陷与 interpolate-size/height:auto 新方案对比
- name 属性原生互斥 + JS 兜底
- summary marker 隐藏与箭头旋转
