---
title: [RBL-593] 笔试：手写 Tarjan 强连通分量（迭代版防栈溢出）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-593：笔试：手写 Tarjan 强连通分量（迭代版防栈溢出）

**答**：实现 `tarjan(nodes, edges)`，nodes 为 id 数组，edges: `Map<id, id[]>`。返回 SCC 数组（每项为 id 数组）。要求：迭代实现（显式栈，防大图递归爆栈）；SCC 内节点按发现顺序；结果顺序任意但完整性正确。边界：自环（a->a 计为长度 1 的 SCC，不与普通单点区分也需正确）；孤立节点；空图。

```javascript
function tarjan(nodes, edges) {
  const idx = new Map(), low = new Map(), onStack = new Set(), stack = [];
  const sccs = []; let counter = 0;

  for (const start of nodes) {
    if (idx.has(start)) continue;
    // 显式栈帧：{ v, edgeIdx }，模拟递归
    const call = [{ v: start, i: 0 }];
    idx.set(start, counter); low.set(start, counter); counter++;
    stack.push(start); onStack.add(start);

    while (call.length) {
      const frame = call[call.length - 1];
      const outs = edges.get(frame.v) || [];
      if (frame.i < outs.length) {
        const w = outs[frame.i++];
        if (!idx.has(w)) {                        // 树边：展开
          idx.set(w, counter); low.set(w, counter); counter++;
          stack.push(w); onStack.add(w);
          call.push({ v: w, i: 0 });
        } else if (onStack.has(w)) {              // 回边：更新 low
          low.set(frame.v, Math.min(low.get(frame.v), idx.get(w)));
        }
      } else {
        call.pop();                               // 收尾：回溯更新父 low
        if (call.length) {
          const parent = call[call.length - 1].v;
          low.set(parent, Math.min(low.get(parent), low.get(frame.v)));
        }
        if (low.get(frame.v) === idx.get(frame.v)) {   // 根：弹出 SCC
          const comp = []; let w;
          do { w = stack.pop(); onStack.delete(w); comp.push(w); } while (w !== frame.v);
          sccs.push(comp);
        }
      }
    }
  }
  return sccs;
}

// 自测
// 图: a<->b, b->c, c->a (a,b,c 一个环), d->a, e 孤立
const edges = new Map([
  ['a', ['b']], ['b', ['a', 'c']], ['c', ['a']], ['d', ['a']], ['e', []]],
);
const sccs = tarjan(['a', 'b', 'c', 'd', 'e'], edges).map(s => [...s].sort());
// 断言：存在长度 3 的 SCC（a,b,c）；d、e 是单点 SCC
console.log(sccs.some(s => s.length === 3), sccs.filter(s => s.length === 1).length === 2);

// 自环
console.log(tarjan(['x'], new Map([['x', ['x']]])));   // [['x']]，不崩

// 大图栈安全：10 万节点链
const big = new Map(); for (let i = 0; i < 99999; i++) big.set(i, [i + 1]); big.set(99999, []);
const t0 = Date.now(); const r = tarjan([...big.keys()], big);
console.log(r.length === 100000, Date.now() - t0 < 1000);   // 迭代版不爆栈
```

**评分点**：
- Tarjan 三要素正确：low/index 更新、回边判定用 onStack、根条件 low===idx
- 迭代化正确：显式栈帧带边指针，回溯时向父帧传播 low（漏掉此步是最常见 bug）
- 自环、孤立点、空图边界不崩；超大图（10 万节点）不爆栈
- 能指出「SCC 结果即环内缩点，产物顺序在 SCC 内另行决策」属于加分
