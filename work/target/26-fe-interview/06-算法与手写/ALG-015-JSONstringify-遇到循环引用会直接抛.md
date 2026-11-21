---
title: [ALG-015] `JSON.stringify` 遇到循环引用会直接抛 `TypeError: Converting circular structure to JSON`，上传用户数据前需要先检测。如何判断一个对象是否存在循环引用？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-015：`JSON.stringify` 遇到循环引用会直接抛 `TypeError: Converting circular structure to JSON`，上传用户数据前需要先检测。如何判断一个对象是否存在循环引用？
**答**：DFS 遍历对象图，用 `WeakSet` 记录"当前递归路径"上的节点；再次遇到路径上的同一引用即为环。`WeakSet` 不阻止垃圾回收；回溯时删除节点可以区分"环"与"普通的共享子对象（DAG）"。时间 O(n)，空间 O(n)。

```javascript
function hasCycle(obj) {
  const onPath = new WeakSet();
  function dfs(cur) {
    if (cur === null || typeof cur !== 'object') return false;
    if (onPath.has(cur)) return true;   // 回到了路径上的节点，成环
    onPath.add(cur);
    for (const key of Object.keys(cur)) {
      if (dfs(cur[key])) return true;
    }
    onPath.delete(cur); // 回溯；不删则会把共享引用也误报为环
    return false;
  }
  return dfs(obj);
}
```
