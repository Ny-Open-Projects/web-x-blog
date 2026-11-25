---
title: [WCN-280] Signals 调度与并发收束（面试答法）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-280：Signals 调度与并发收束（面试答法）。
**答**：
- 核心机制：写→标脏→微任务批量 flush→拓扑序重算→effect 执行——批处理是性能本质。
- 并发协同：与框架 transition 双缓冲、优先级分桶、直写逃逸通道。
- 正确性红线：computed 纯函数、循环检测、effect 清理、异步 epoch 竞态。
- 演进方向：TC39 语言级信号统一跨框架语义——自有库向提案对齐。

```javascript
const signalsCore = {
  pipeline: 'write → dirty → batch flush → topo recompute → effects',
  concurrency: ['transition 双缓冲', '优先级分桶', '直写逃逸'],
  redlines: ['computed 纯函数', '循环检测', 'cleanup/dispose', 'epoch 竞态'],
  future: 'TC39 Signals 对齐',
};
r
```
