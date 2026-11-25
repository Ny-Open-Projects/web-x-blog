---
title: [JS-332] 内存快照分析方法：三快照法与 Retainer 链
date: 2026-11-21
categories: [JavaScript]
tags: [前端面试, 面试题, V8]
type: 面试题
---

## JS-332：内存快照分析方法：三快照法与 Retainer 链

**答**：
- 三快照法：快照 A → 执行可疑操作 N 次 → 快照 B → 再操作一次 → 快照 C；对比 A/B 找增量对象，用 C 过滤「稳定增长的真泄漏」（B 与 C 都存在且增长）
- Retainer 链：快照中选中泄漏对象 → Retainers 面板看保留路径——定位「谁挂着它」（distance 越小越接近根，routers: GC roots/window/timer）
- 视图技巧：Summary 按 constructor 分组（看 detached 的构造器：Detached HTMLDivElement）、Comparison 视图看增减、Containment 看整体结构；过滤 `Detached` 关键字是查 DOM 泄漏捷径
- 常见泄漏指纹：Detached 节点数组、闭包 Context 堆积、未清理的 Map（key 是 DOM）、数组无限 push
- 现代工具补充：performance.measureMemory()（Chrome）按 breakDown 维度看分配、allocation timeline（按分配位置定位热点）

```text
快照操作流:
  1. Memory 面板 → Take Snapshot (A)
  2. 执行 10 次可疑交互
  3. Take Snapshot (B) → 选 Comparison vs A → 看 #Delta
  4. 再执行 1 次 → Snapshot (C)
  5. C 中搜索 Detached → Retainers 找挂载者 → 定位代码
```
