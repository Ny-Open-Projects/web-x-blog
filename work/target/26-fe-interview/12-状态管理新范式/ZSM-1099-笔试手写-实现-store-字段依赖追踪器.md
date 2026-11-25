---
title: [1099] 笔试手写：实现 store 字段依赖追踪器
date: 2026-11-22
categories: [状态管理新范式]
tags: [前端面试, 笔试题, Zustand]
type: 笔试题
---

## 1099：笔试手写：实现 store 字段依赖追踪器

**答**：实现 trackDeps(actions)：actions 为 { name, run: (get, set) => void, getFields: string[], setFields: string[] }[]（笔试用声明代替运行时 Proxy 追踪）。输出 action × field 的写入矩阵、每个 field 的写入者列表，并给出影响面报告：哪些 field 被多个 action 写（有并发风险）。返回 { matrix, writers, multiWrite }。

```js
function trackDeps(actions) {
  const matrix = {}, writers = {};
  for (const a of actions) {
    matrix[a.name] = {};
    for (const f of a.setFields) {
      matrix[a.name][f] = true;
      (writers[f] ??= []).push(a.name);
    }
    for (const f of a.getFields) if (!matrix[a.name][f]) matrix[a.name][f] = 'r'; // 读标记
  }
  const multiWrite = Object.entries(writers)
    .filter(([, ws]) => ws.length > 1)
    .map(([f, ws]) => ({ field: f, writers: ws }));
  return { matrix, writers, multiWrite };
}
```

**评分点**：
- field 级写入者归集（影响面分析的数据基础）
- multiWrite 是竞态与 UI 抖动的预警信号
- 读写区分标记（只读依赖不误报）
- 能讨论：真实实现用 Proxy 拦截 set 收集，声明式是笔试简化
