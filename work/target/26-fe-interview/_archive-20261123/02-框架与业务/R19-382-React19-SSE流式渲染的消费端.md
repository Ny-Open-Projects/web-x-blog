---
title: [R19-382] React19 流式渲染的消费端：Suspense 与 chunk 到达
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, SSR]
type: 面试题
---

## R19-382：React19 流式渲染的消费端：Suspense 与 chunk 到达

**答**：
- 消费端三件事：解析 Flight 流（chunk 到达逐个 resolve promise 槽位）、Suspense 占位替换、渐进水合
- chunk 到达顺序与 UI 顺序无关：先到先显示（自上而下也可能乱序）——布局稳定性设计（占位高度预留防 CLS）
- React 19 的 ViewTransition + 流式：chunk 插入带转场动画（实验）——流式内容「淡入」而非跳变
- 性能要点：chunk 尺寸与 HTML flush 频率——过大 chunk 延迟首屏，过碎增加流解析开销；按 Suspense 边界粒度均衡
- 监控：首字节 → 各 chunk 到达时间分布 → 全部水合完成——流式渲染的瀑布分析指标

```text
流式时间线:
  t0 首字节(shell+fallback)
  t1 chunk#1(导航) → 水合导航
  t2 chunk#2(商品卡) → 替换占位
  t3 全部完成 → TTI
指标: chunk 间隔 / 占位停留时长 / CLS
```
