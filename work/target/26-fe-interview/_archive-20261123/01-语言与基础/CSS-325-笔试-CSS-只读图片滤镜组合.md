---
title: [CSS-325] 笔试：CSS 图片滤镜组合（filter 实战）
date: 2026-11-19
categories: [CSS]
tags: [前端面试, 笔试题, 效果]
type: 笔试题
---

## CSS-325：笔试：CSS 图片滤镜组合

**题目**：实现：① 黑白 hover 恢复彩色 ② 暗色主题下图片自动压暗 ③ 玻璃质感毛玻璃卡片（背后内容可见）④ 滤镜动画渐变过渡。

**答**：
```css
/* ① 黑白 hover 彩色 */
.photo { filter: grayscale(1); transition: filter .4s; }
.photo:hover { filter: grayscale(0); }

/* ② 暗色主题压暗：brightness + 轻微降饱和，避免刺眼 */
[data-theme='dark'] .photo { filter: brightness(.8) contrast(1.05); }

/* ③ 毛玻璃卡片 */
.glass {
  background: rgb(255 255 255 / .6);
  backdrop-filter: blur(12px) saturate(1.4);
  border: 1px solid rgb(255 255 255 / .4);
  border-radius: 16px;
}

/* ④ 多滤镜链与过渡（filter 值列表整体插值） */
.duo {
  filter: brightness(1.1) sepia(.3);
  transition: filter .6s;
}
.duo:hover { filter: brightness(1) sepia(0); }

/* 组合顺序说明：filter 从左到右依次作用于结果 */
```

**评分点**：
- grayscale/brightness/sepia 的语义与链式组合（顺序影响结果）
- 暗色主题图片压暗是「无图源改动」的通用方案（brightness + contrast）
- backdrop-filter 与 filter 的对象差异（背后内容 vs 自身）
- transition 作用于 filter 的插值前提（函数列表一致）
