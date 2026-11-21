---
title: [HW-120] 手写循环安全的对象遍历器——WeakSet 防环 + 访问路径记录 + 引用计数统计
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：遍历任意嵌套对象（可能成环）的通用遍历器：WeakSet 记录"当前 DFS 栈上的对象"防环（比 WeakMap 记全局更精确——同一对象在不同分支出现应各自遍历）；带访问路径（a.b[0].c）；可选统计（节点类型计数/最大深度）。

```javascript
function walkSafe(root, { visit, maxDepth = Infinity } = {}) {
  const onStack = new WeakSet();                  // DFS 栈：同一分支内防环
  const stats = { nodes: 0, maxDepth: 0 };

  function dfs(value, path, depth) {
    stats.nodes++;
    stats.maxDepth = Math.max(stats.maxDepth, depth);
    visit?.(value, path, depth);
    if (value === null || typeof value !== 'object' || depth >= maxDepth) return;
    if (onStack.has(value)) { visit?.(value, path + ' <circular>', depth); return; }   // 成环
    onStack.add(value);
    try {
      if (Array.isArray(value)) {
        value.forEach((v, i) => dfs(v, `${path}[${i}]`, depth + 1));
      } else {
        for (const [k, v] of Object.entries(value)) dfs(v, path ? `${path}.${k}` : k, depth + 1);
      }
    } finally {
      onStack.delete(value);                      // 回溯：弹出栈（允许其他分支再次访问）
    }
  }
  dfs(root, '', 0);
  return stats;
}
// 验证：const a = { list: [] }; a.list.push(a); a.list.push({ name: 'x' });
// walkSafe(a, { visit: (v, p) => console.log(p) })
// => list[0] <circular>（环标记）；list[1].name = 'x'（环不阻断其他分支）
// WeakSet 而非 WeakMap：只需"在不在栈上"的布尔语义，且不阻止 GC
```

**评分点**：
- WeakSet 当 DFS 栈用（回溯时 delete），同一对象跨分支可重复访问——比"全局已访问"语义更正确。
- 环标记输出（path + <circular>）而非静默跳过。
- 路径记录与 stats（maxDepth）。
- WeakSet vs WeakMap 的语义差异说清。
