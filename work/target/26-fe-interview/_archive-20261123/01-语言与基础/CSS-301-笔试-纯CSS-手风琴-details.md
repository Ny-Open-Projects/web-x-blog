---
title: [CSS-301] 笔试：纯 CSS 手风琴（details + 动画）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 组件]
type: 笔试题
---

## CSS-301：笔试：纯 CSS 手风琴

**题目**：用 `<details>` 实现手风琴：带展开/收起动画、箭头旋转、同一时刻只展开一项、无障碍保留（键盘可用）。

**答**：
```css
.acc { border-bottom: 1px solid #eee; }
.acc summary {
  display: flex; justify-content: space-between; align-items: center;
  cursor: pointer; padding: 14px 0; font-weight: 600;
  list-style: none;
}
.acc summary::-webkit-details-marker { display: none; }
.acc .arrow { transition: transform .3s; }
.acc[open] .arrow { transform: rotate(180deg); }

/* 高度动画：grid 0fr/1fr（兼容性最好的 auto 高度动画） */
.acc .body {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows .3s;
  overflow: hidden;
}
.acc[open] .body { grid-template-rows: 1fr; }
.acc .body > div { overflow: hidden; }

/* 内容淡入错峰 */
.acc[open] .body > div { animation: fade .3s .1s both; }
@keyframes fade { from { opacity: 0; } }
```
```html
<!-- name 属性：同名 details 自动互斥（同刻只开一项），原生无障碍 -->
<details class="acc" name="faq">
  <summary>问题一 <span class="arrow">▾</span></summary>
  <div class="body"><div>答案内容……</div></div>
</details>
<details class="acc" name="faq">
  <summary>问题二 <span class="arrow">▾</span></summary>
  <div class="body"><div>答案内容……</div></div>
</details>
```

**评分点**：
- details[name] 原生互斥（互斥不靠 JS）——新标准关键点
- grid 0fr/1fr 动画高度（不用 JS 量高度）
- summary 的默认 marker 清除与箭头旋转联动 [open]
- list-style: none 保留键盘/读屏可访问性
