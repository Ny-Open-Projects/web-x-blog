---
title: [WCN-935] 改一个 semantic token 会影响哪些组件和页面：怎么做变更影响面分析
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-935：改一个 semantic token 会影响哪些组件和页面：怎么做变更影响面分析

**答**：
- 结论先行：token 变更影响面靠「依赖图 + 血缘（lineage）」回答——建三层图：token→组件、组件→页面、页面→业务域，改一个 token 沿图正向传播得到受影响集合。
- 数据来源：token→组件从代码静态分析（扫描 var(--token) / 引用路径）得到；组件→页面从组件使用热力图或 import 关系得到；缺一都会漏判。
- 分级评估：区分「直接引用（强影响）」与「间接继承（弱影响）」，结合覆盖率判断回归测试范围（设计系统平台治理常见）。
- 自动化：CI 在 token PR 里自动产出影响报告 + 触发相关视觉回归用例，未覆盖的受影响页面要求补测。
- 追问钩子：面试官问「循环依赖的 token 血缘怎么算」——答：血缘图应是 DAG，出现环说明 token 设计有循环引用，先修设计再算影响面。

```javascript
// token 影响面：正向传播
const graph = {
  'color.link': ['ds-button', 'ds-breadcrumb'],
  'ds-button':  ['/cart', '/checkout'],
  'ds-breadcrumb': ['/product'],
};
function impact(token, graph) {
  const seen = new Set(), queue = [token];
  while (queue.length) {
    const k = queue.shift();
    for (const next of graph[k] || []) if (!seen.has(next)) { seen.add(next); queue.push(next); }
  }
  return [...seen];
}
console.log(impact('color.link', graph));
// ['ds-button', 'ds-breadcrumb', '/cart', '/checkout', '/product']
```
