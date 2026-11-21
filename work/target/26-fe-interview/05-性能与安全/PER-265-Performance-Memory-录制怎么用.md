---
title: [PER-265] Performance 面板的内存曲线怎么看？JS Heap / Nodes / Listeners 曲线各说明什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-265：Performance 面板的内存曲线怎么看？JS Heap / Nodes / Listeners 曲线各说明什么？

**答**：
- 打开 Memory 勾选项录制：出现四条曲线——JS Heap（JS 堆大小）、Documents、Nodes（DOM 节点数）、Listeners（事件监听器数）。锯齿状上下波动是正常 GC 节奏；持续阶梯上涨不回落才是泄漏。
- 各曲线的诊断意义：Nodes 上涨不落 → DOM 泄漏（detached 节点被引用）；Listeners 单调上涨 → 监听器泄漏（每次操作 addEventListener 没 remove）；JS Heap 涨 → 闭包/缓存类泄漏，转堆快照定位。
- 配合操作：录制时标注操作区间（点标记按钮），反复执行同一操作，观察每个区间的"操作前基准—GC 后回落点"，回落点不断抬高即泄漏。
- 与 Allocation instrumentation 的关系：曲线告诉你"有没有"，堆分配时间线告诉你"在哪分配的"（按构造函数聚合蓝色柱），两者接力。

```text
录制解读示例（打开/关闭商品详情 ×3）：
JS Heap:   /\  /\  /\   （锯齿，GC 后回到同一水位）        → 正常
Nodes:     850 → 900 → 950 → 1000  （每次 +50 不回落）     → DOM 泄漏
Listeners: 42 → 46 → 50 → 54（每次 +4 不回落）             → 监听器泄漏
→ 堆快照 Comparison：Detached <div class="detail"> +3，Retainers 显示挂在 resize 监听器
→ 修复：unmount 里 removeEventListener('resize', handler) / 用 AbortController
```
