---
title: [ZSM-231] Jotai 的原子依赖图出现循环依赖会怎样怎么排查
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-231：Jotai 的原子依赖图出现循环依赖会怎样，怎么排查

**答**：
- Jotai derived atom 在首次求值时记录依赖边，A 依赖 B、B 又依赖 A 会触发运行时循环检测，抛出 "atom dependency cycle" 错误
- 排查靠 jotai-devtools 的依赖图视图，直接可视化哪些 atom 形成环；没有 devtools 时用 console 追踪 get() 调用栈
- 循环通常是「双向派生」设计错误：想双向同步时应改为「单一真相源 + 写函数派生」，而不是两个 atom 互相 get
- 重构模式：把共同依赖抽成叶子 atom，两个派生只读叶子；需要写回时用 write-only atom 封装更新协议

```javascript
// ❌ 循环
const a = atom((g) => g(b) + 1)
const b = atom((g) => g(a) * 2)   // cycle → 运行时报错

// ✅ 单一真相源
const base = atom(1)
const a = atom((g) => g(base) + 1)
const b = atom((g) => g(base) * 2)
const setBoth = atom(null, (_g, s, v) => s(base, v))  // 写路径统一
```
