---
title: [R19-386] 子节点 diff 算法深水：两轮遍历与 key 复用
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, Fiber]
type: 面试题
---

## R19-386：子节点 diff 算法深水：两轮遍历与 key 复用

**答**：
- 第一轮（按位置）：old 与 new 同索引对比——key 相同或（都无 key 且 type 相同）→ 复用 patch；不匹配则中断进入第二轮
- 第二轮（按 key）：old 剩余节点建 Map<key, fiber>——new 剩余节点逐个查 Map：命中 → 复用（标记 Placement 移动），未命中 → 新建，Map 里剩下的 → Deletion
- Placement 的移动策略：React 用「最后位置锚点」——比较 oldIndex 顺序，乱序节点按 new 顺序插入到正确锚点前（insertBefore），一次遍历完成插入
- 为什么不用 LIS：Vue3 用 LIS 最小移动；React 用「从后向前锚点插入」——移动次数可能略多但实现简单；这是两大框架 diff 的核心差异点
- key 设计影响：稳定 key → 全部命中复用；index key → 头部插入时第二轮全量移动；无 key → 只按位置 patch（状态错乱风险）

```text
old: [A, B, C, D]  new: [D, A, B, C]
第一轮: A≠D 中断
第二轮: Map{A,B,C,D}; D 命中移到最前(anchor=头), A/B/C 命中
结果: 移动 1 次 (D 提前), A/B/C 原位
```
