---
title: [TST-998] 一个 PR 同时改了 3 个子应用的契约，门禁的「影响面」怎么算才不漏？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-998：一个 PR 同时改了 3 个子应用的契约，门禁的「影响面」怎么算才不漏？
**答**：
- 结论：用「依赖图传播」算影响面——从改动文件出发，沿契约依赖边传播到所有消费者（直接+间接），取并集作为门禁范围。
- 做法：构建 模块→契约→消费者 的有向图；改了提供者契约则所有消费者子应用的用例必须跑；影响面越大门禁等级越高。
- 边界：循环依赖要检测并人工介入；无法解析的动态依赖按最保守处理。
- 追问钩子：PR 只改了一个公共枚举，但要跑 20 个子应用，研发抱怨太慢，你怎么既快又不漏？

```javascript
function impactScope(changed, graph) {
  const visited = new Set(), queue = [...changed];
  while (queue.length) {
    const node = queue.shift();
    if (visited.has(node)) continue;
    visited.add(node);
    queue.push(...(graph[node] || [])); // 沿依赖边传播
  }
  return [...visited];
}
const graph = {
  'enum.js': ['cart-contract', 'pay-contract'],
  'cart-contract': ['app-cart', 'app-promotion'],
  'pay-contract': ['app-pay'],
};
const affected = impactScope(['enum.js'], graph);
console.log(affected); // ['enum.js','cart-contract','pay-contract','app-cart','app-promotion','app-pay']
const level = affected.length > 10 ? 'high' : affected.length > 3 ? 'medium' : 'low';
console.log(level); // 'medium' → 影响 6 个节点
```
