---
title: [OPT-081] 怎么用 Profiler 火焰图定位"渲染风暴"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-081：怎么用 Profiler 火焰图定位"渲染风暴"？

**答**：
- React DevTools Profiler 录制交互，火焰图里每个灰色块是一次提交（commit），块越宽耗时越长；开启 "Highlight updates" 能直接看到哪些组件在闪。
- 定位三板斧：看 commit 排行（按 duration 排序）→ 点进宽块看 "Why did this render?"（props/state/parent/context 变化原因）→ 对比 "actual duration" 与基线。
- 典型风暴：一个高频变化的状态放在树顶，导致整棵树每帧重渲；火焰图表现为大量等宽条带。
- 修复后用 Profiler 的 "Record why each component rendered" 复录对比，确认重渲染数量下降，而不是靠感觉。

```jsx
// 一一对应：Profiler API 程序化定位渲染风暴（可写进测试）
import { Profiler } from 'react';

// 1. 包住可疑子树，收集每次提交的耗时与原因
function onRender(id, phase, actualDuration, commits, interactions) {
  if (actualDuration > 16) { // 超过一帧预算的提交才记录，降噪
    report('react-commit', {
      subtree: id,
      phase,           // mount | update
      actualMs: Number(actualDuration.toFixed(1)),
    });
  }
}

<Profiler id="GoodsList" onRender={onRender}>
  <GoodsList items={items} keyword={keyword} />
</Profiler>

// 2. 常见风暴现场：keyword 放在顶层，每敲一个字整棵树重渲
// <App>                     <- keyword 在这
//   <Header />              <- 与 keyword 无关却跟着重渲
//   <GoodsList items={} />  <- 1000 行全量重渲
// 修复后结构见 OPT-082/OPT-083：把 keyword 下沉到搜索组件局部 + memo 边界

// 3. Profiler 面板对照读法：
//    Commit 排行按 Duration 排序 -> 选最宽的块 ->
//    右侧 "Why did this render?" 列出 props changed: keyword ->
//    对应修复就是把 keyword 的消费范围缩小到直接依赖它的组件
```
