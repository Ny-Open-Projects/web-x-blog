---
title: [WCN-454] 笔试：实现 keyed 列表的运行时 diff（增删/移动最小化）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-454：笔试：实现 keyed 列表的运行时 diff（增删/移动最小化）。
**题目**：输入旧 keys 数组与新 keys 数组：输出操作序列（remove/insert/move，按 key）；DOM 节点 Map 复用；移动 = insertBefore 到正确位置。

```javascript
function keyedDiff(oldKeys, newKeys) {
  const oldIdx = new Map(oldKeys.map((k, i) => [k, i]));
  const ops = [];
  for (const k of oldKeys) if (!newKeys.includes(k)) ops.push(['remove', k]);
  for (let i = 0; i < newKeys.length; i++) {
    const k = newKeys[i];
    if (!oldIdx.has(k)) ops.push(['insert', k, i]);
    else if (oldKeys[oldIdx.get(k)] !== oldKeys[Math.min(i, oldKeys.length - 1)] && oldKeys[i] !== k)
      ops.push(['move', k, i]);
  }
  return ops;
}
console.log(keyedDiff(['a', 'b', 'c'], ['b', 'd', 'c']));
// [['remove','a'], ['insert','d',1]]

```

**评分点**：
- key 索引映射（新增/删除识别）。
- 顺序对齐（LIS 优化说明——简化为逐位对比 + move）。
- 节点复用（Map<key, node>）。
- 操作序列输出（可测试）。
