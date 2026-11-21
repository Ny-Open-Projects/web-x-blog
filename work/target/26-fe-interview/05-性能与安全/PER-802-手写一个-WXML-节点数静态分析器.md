---
title: [PER-802] 手写一个 WXML 节点数静态分析器：扫描编译产物统计节点数并输出超标组件
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-802：手写一个 WXML 节点数静态分析器：扫描编译产物统计节点数并输出超标组件

**答**：
- 需求：输入编译产物（wxml 编译后的 js 模块，含节点树结构或标签计数），按页面/组件统计节点总数，输出超过阈值（warn 3000 / danger 5000）的清单与占比；嵌套组件节点数要递归累加到使用它的页面上。
- 边界：组件被多页面复用时分别计入各页面；输出含组件自身节点数与累计节点数两个口径；列表类组件按"单实例节点数 × 重复次数"估算。
- 评分点：递归累加正确；双口径（自身/累计）输出。

```javascript
function analyzeNodes(modules, { warn = 3000, danger = 5000 } = {}) {
  const self = new Map();                       // 模块自身节点数
  for (const m of modules) {
    self.set(m.id, m.nodes ?? countTags(m.source));
  }
  const totalOf = (id, seen = new Set()) => {   // 递归累加（组件引用展开），环检测
    if (seen.has(id)) return 0;
    seen.add(id);
    let sum = self.get(id) || 0;
    for (const child of modules.find(m => m.id === id)?.uses || [])
      sum += totalOf(child, seen);
    return sum;
  };
  return modules.filter(m => m.type === 'page').map(p => ({
    page: p.id, selfNodes: self.get(p.id), totalNodes: totalOf(p.id),
    verdict: totalOf(p.id) > danger ? 'danger' : totalOf(p.id) > warn ? 'warn' : 'ok',
  })).sort((a, b) => b.totalNodes - a.totalNodes);
}
function countTags(source) { return (source.match(/<\w+/g) || []).length; }
```
