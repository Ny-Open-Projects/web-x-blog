---
title: [BAS-173] CSSOM 和关键渲染路径是什么关系？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-173：CSSOM 和关键渲染路径是什么关系？
**答**：
- 关键渲染路径：HTML 解析成 DOM、CSS 解析成 CSSOM → 两者合成渲染树 → Layout 算几何 → Paint 绘制上屏。
- CSSOM 构建完成前浏览器不渲染（CSS 阻塞渲染），这就是"首屏关键 CSS 内联"优化的依据。
- JS 会阻塞 DOM 解析（同步脚本），而渲染树不含 display:none 节点和 head，但含伪元素。

```html
<!-- 关键渲染路径四步 -->
<!-- 1. 解析 HTML 建 DOM；解析 CSS 建 CSSOM，CSSOM 没建完不渲染 -->
<!-- 2. DOM + CSSOM 合成渲染树，display:none 与 head 不进树，伪元素会进 -->
<!-- 3. Layout 计算几何，4. Paint 绘制、Composite 合成上屏 -->
<link rel="stylesheet" href="critical.css" />
<!-- 优化点：压缩阻塞资源、首屏 CSS 内联、非关键 CSS 异步加载 -->
```
