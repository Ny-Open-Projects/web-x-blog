---
title: [CSS-315] 笔试：CSS 渐变边框与边框内圆角
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 效果]
type: 笔试题
---

## CSS-315：笔试：渐变边框与边框内圆角

**题目**：实现：① 渐变色边框（圆角保留）② 经典「内圆角」：外框圆角 R，内框圆角 = R - padding。各给两种实现。

**答**：
```css
/* 渐变边框方案一：border-image（不支持 border-radius，弃用提示） */
/* 渐变边框方案二：双层背景剪裁（保留圆角，推荐） */
.gradient-border {
  border: 2px solid transparent;
  border-radius: 12px;
  background:
    linear-gradient(#fff, #fff) padding-box,          /* 内容区 */
    linear-gradient(90deg, #4285f4, #ea4335) border-box; /* 边框区 */
}

/* 渐变边框方案三：outline/伪类 */
.gb2 {
  position: relative; border-radius: 12px;
}
.gb2::before {
  content: ''; position: absolute; inset: -2px;
  border-radius: 14px;
  background: linear-gradient(90deg, #4285f4, #ea4335);
  z-index: -1;
}

/* 内圆角：数学关系 */
.outer {
  border-radius: 16px;
  padding: 6px;
  background: #333;
}
.inner { border-radius: 10px; }  /* 16 - 6 = 10，同心圆角 */
```

**评分点**：
- 双层 background + padding-box/border-box 的剪裁原理（渐变边框标准解）
- border-image 不支持 border-radius 的坑
- 伪类方案的 z-index 与负 inset
- 内圆角公式「内 = 外 - padding」及同心证明
