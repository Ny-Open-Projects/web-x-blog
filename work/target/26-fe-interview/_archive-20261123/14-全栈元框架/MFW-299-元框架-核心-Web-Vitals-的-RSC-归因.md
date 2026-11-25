---
title: [MFW-299] Core Web Vitals 的 RSC 归因（哪段代码伤了指标）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## MFW-299：CWV 的 RSC 归因

**答**:
- LCP 归因分账：图片（priority/尺寸）→ TTFB 段（RSC DB 慢）→ hydration 挤占（大 client 树阻塞渲染）——三段各自埋点（MFW-265 预算分账的 CWV 版）
- INP 与 RSC 关系：交互后触发 Action/router.refresh 的长任务——Action RTT + 重渲染 diff 计算 = INP 主要构成；优化：乐观更新先绘（useOptimistic）+ 精准失效（不整树 refresh）
- CLS 元框架特有源：流式 Suspense 高度跳动（骨架与内容尺寸差）——骨架按最终内容尺寸预留（布局模板一致性）；字体 swap 窗口（next/font 已治）
- 归因工具链：RUM 按路由聚合 CWV + 与构建版本 join（哪次发布劣化了哪个路由的 LCP——版本维度回归检测）

```text
归因表：LCP = 图/TTFB/hydration 三段埋点；INP = ActionRTT+重渲染（乐观先绘治）
CLS：骨架=最终尺寸；字体 next/font
闭环：RUM × 构建版本 join → 回归自动定位发布
```
