---
title: [BLD-254] 构建确定性与随机源治理怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-254：随机源治理怎么做？
**答**：
- 随机源清单：模块处理顺序（多线程完成顺序不定——影响合并顺序）、Map 遍历序（依赖插入序）、Math.random（构建期脚本）、Set/对象键序——任何进入产物的「顺序敏感」输出。
- 治理：输出排序（所有进入产物的集合统一排序——sort keys）、模块 ID 确定（SCN-BLD-219 deterministic IDs）、构建脚本禁 Math.random（lint 构建期代码）。
- 检测：双次构建 diff（SCN-BLD-224）——非确定源残留即暴露。
- 确定性的价值链：可复现构建 → 产物 hash 可信（审计）→ 缓存键稳定（命中）→ diff 噪声归零（评审）。
- 追问钩子：为什么「多线程完成顺序」会污染产物——并行转换多个模块时，谁先完成谁先进入合并队列；合并顺序影响拼接产物（chunk 内模块顺序）→ 产物字节不同 → hash 不同 → 缓存/审计/diff 全部失真；治理是「完成后再按确定序合并」——并行执行、串行合并。

```javascript
// 并行执行 + 确定序合并
const results = await Promise.all(modules.map(transform));   // 并行转换
const ordered = results.sort((a, b) => a.id.localeCompare(b.id));   // 确定序合并
emit(ordered);
// Map 遍历序治理
Object.keys(obj).sort().forEach(...)                   // 进入产物的集合一律排序
```
