---
title: [WCN-258] 信号的序列化边界（哪些能序列化/如何处理不可序列化值）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-258：信号的序列化边界（哪些能序列化/如何处理不可序列化值）？
**答**：
- 可序列化：原始值/JSON 兼容对象——跨端（SSR/存储）传输无碍。
- 不可序列化：函数/Map/Set/类实例——标记为「客户端专属」，SSR 快照跳过。
- 恢复策略：可序列化部分 restore，客户端专属部分懒初始化（首次访问时计算）。
- 版本：快照带 schema 版本，字段变更走迁移函数。

```javascript
const sig = signal(new Map(), { serialize: false });   // 客户端专属
// 快照只含 serialize !== false 的信号
const snap = Object.fromEntries(registry.filter(s => s.serialize !== false)
  .map(s => [s.id, s.value]));
r
```
