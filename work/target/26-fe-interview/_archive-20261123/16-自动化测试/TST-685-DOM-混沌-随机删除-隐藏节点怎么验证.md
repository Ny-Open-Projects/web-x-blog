---
title: [TST-685] DOM 混沌：随机删除 / 隐藏节点怎么验证应用健壮性？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-685：DOM 混沌：随机删除 / 隐藏节点怎么验证应用健壮性？

**答**：
- 结论：DOM 混沌验证「界面局部损坏时核心流程不崩」——随机隐藏非关键节点、删除列表项、篡改文本。
- 注入后断言：无 JS 异常、核心按钮可点、错误边界正确降级。
- 关键节点（提交按钮）设白名单，避免把测试自己搞挂。
- 追问钩子：隐藏节点后 React 抛错，说明组件有什么问题？

```javascript
function domChaos(root, { rate = 0.2, keep = ['button[type=submit]'] } = {}) {
  const nodes = [...root.querySelectorAll('*')]
    .filter(n => !keep.some(s => n.matches(s)));
  const removed = [];
  nodes.forEach(n => {
    if (Math.random() < rate) {
      const parent = n.parentNode;
      parent.removeChild(n);
      removed.push({ node: n, parent });
    }
  });
  return () => removed.forEach(({ node, parent }) =>
    parent.insertBefore(node, null));
}
```
