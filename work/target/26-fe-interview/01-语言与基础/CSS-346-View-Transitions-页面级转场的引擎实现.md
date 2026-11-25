---
title: [CSS-346] View Transitions：页面级转场的引擎实现
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 动画]
type: 面试题
---

## CSS-346：View Transitions：页面级转场的引擎实现

**答**：
- 机制：document.startViewTransition(callback) 触发时——引擎先截取旧状态快照（伪元素 ::view-transition-old），执行 DOM 更新回调，再截取新状态快照（::view-transition-new），对每张快照用 CSS 动画交叉过渡
- 成本模型：快照是位图（整页或按 view-transition-name 分组），过渡期间页面是「冻结的位图动画」——期间主线程可以继续工作，但用户看到的中间态不是真实 DOM
- 分组命名：给元素设 view-transition-name，各自独立快照独立动画——卡片飞到详情页的「共享元素转场」靠同名跨状态匹配
- 同文档 vs 跨文档：SPA 用 startViewTransition + 更新 DOM；MPA 用 @view-transition { navigation: auto }（Chrome 126+），浏览器在导航时自动截快照
- 定制：::view-transition-group/old/new/image-pair 各伪元素可改动画（时长/缓动/位置），配合 view-transition-class 批量定制；旧状态不支持时直接降级为瞬时切换（catch 分支）

```javascript
function switchTab(id) {
  if (!document.startViewTransition) { updateTab(id); return; }  // 降级
  document.startViewTransition(() => updateTab(id));
}
```

```css
/* 共享元素转场: 列表卡片 → 详情头图 */
.card__img { view-transition-name: hero-img; }
.detail__img { view-transition-name: hero-img; }
/* 批量定制 */
::view-transition-group(*) { animation-duration: .3s; }
```
