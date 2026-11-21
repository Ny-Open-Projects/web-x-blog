---
title: [WCN-242] Signal 依赖图的重算顺序如何保证正确（拓扑）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-242：Signal 依赖图的重算顺序如何保证正确（拓扑）？
**答**：
- 方案 A（Solid 风格）：每个节点记 epoch/version，effect 检查依赖版本是否大于自己上次读取——pull 式惰性验证。
- 方案 B（显式拓扑）：flush 前对 dirty 集合做拓扑排序（依赖者后算）。
- 环检测：响应式系统禁止循环依赖——创建/读取时检测环并抛错。
- 复杂度：惰性验证不排序但可能重复探测；显式排序一次算清但排序本身有成本。

```javascript
// 惰性验证（pull 模式）
function readComputed(node) {
  if (node.dirty) { for (const d of node.deps) readComputed(d); // 先推平依赖
    node.value = node.compute(); node.dirty = false; }
  return node.value;
}
// 环检测：创建依赖边时 DFS 检查是否会回环
r
```
