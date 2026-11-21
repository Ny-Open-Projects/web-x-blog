---
title: [ALG-029] 画布工具保存了两份组件树快照，需要判断"子树 A 是否作为子结构出现在快照 B 中"（用于树搜索高亮/模板复用检测）。如何判断子树匹配？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-029：画布工具保存了两份组件树快照，需要判断"子树 A 是否作为子结构出现在快照 B 中"（用于树搜索高亮/模板复用检测）。如何判断子树匹配？
**答**：把每个子树序列化成唯一字符串（值 + 括起来的孩子序列），两串相等当且仅当结构完全相同。对大树的每个节点做同样序列化并与目标串比较。优化点：自底向上算哈希可降到 O(n)。时间 O(n × m)，空间 O(n × m)。

```javascript
const serializeSub = node => {
  if (!node) return '#';
  return node.label + '(' + (node.children || []).map(serializeSub).join(',') + ')';
};
function containsSubtree(root, sub) {
  if (!root) return false;
  if (serializeSub(root) === serializeSub(sub)) return true; // 以 root 为根完全匹配
  return (root.children || []).some(c => containsSubtree(c, sub));
}
```
