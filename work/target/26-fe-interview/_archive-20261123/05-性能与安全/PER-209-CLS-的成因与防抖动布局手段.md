---
title: [PER-209] CLS 的成因有哪些？如何在布局层预防抖动？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-209：CLS 的成因有哪些？如何在布局层预防抖动？

**答**：
- 高频成因：无尺寸的图片/视频/iframe（加载后撑开）、动态注入的 banner/弹层把内容顶下去、web 字体换字体导致 FOUT 重排、异步内容插入到已有内容上方、动画用 top/left 触发布局位移。
- 预防手段：媒体元素一律声明 `width/height` 或 CSS `aspect-ratio` 预留占位；广告位、公告栏用固定 min-height 占坑；字体用 size-adjust 度量对齐减少换字重排；动态内容插入到文档流下方或用 overlay 定位不挤占布局。
- 动画只用 transform/opacity（合成器线程执行，不触发 layout）；骨架屏应与真实内容结构尺寸一致，否则"骨架屏本身制造 CLS"。
- 注意口径：CLS 会话窗口内 5 秒内累计的最大 burst，且 `hadRecentInput`（用户输入后 500ms 内）的位移不计入——所以"用户点了才弹出的层"不算 CLS，自动弹出的算。

```css
/* 预防性布局样板 */
.hero img { width: 100%; height: auto; aspect-ratio: 16 / 9; }  /* 显式比例占位 */
.ad-slot  { min-height: 250px; contain: layout; }               /* 广告占坑不塌陷 */
@keyframes slide { from { transform: translateY(20px); } to { transform: none; } }
.banner   { animation: slide .3s; }                             /* 动画走 transform 不触发 layout */
```
