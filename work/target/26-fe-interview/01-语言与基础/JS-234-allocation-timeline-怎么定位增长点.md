---
title: [JS-234] allocation timeline 怎么定位增长点
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## JS-234：allocation timeline 定位增长点

**答**：
- Allocation instrumentation on timeline：边操作边录「分配时间线」，蓝色柱 = 该时刻分配且仍存活的对象
- 与快照法的分工：快照法答「谁泄漏」，timeline 答「哪次操作/哪行代码分配的」——定位代码行更快
- 操作流程：开始记录 → 复现操作序列 → 停止 → 找出「反复出现的蓝柱」→ 点开看构造函数与分配栈
- 归因输出：分配栈直接指向源码行（配合 source map）——比三快照法少一轮猜测
- 注意：录制期间性能开销大，只用于开发环境复现

```text
Memory 面板 → Allocation instrumentation on timeline →
开始录制 → 重复执行可疑操作 → 停止 →
蓝色柱按 Constructor 分组 → 点选反复增长的对象 →
底部 Allocation stack 显示分配时的调用栈（定位到行）
```
