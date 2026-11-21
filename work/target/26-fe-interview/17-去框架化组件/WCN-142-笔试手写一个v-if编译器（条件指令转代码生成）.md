---
title: [WCN-142] 笔试：手写 v-if 指令编译器（条件节点 → createIf 调用代码生成）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 编译器方向]
type: 笔试题
---

## WCN-142：笔试：手写 v-if 指令编译器

**题目**：输入节点树 `{ type:'div', props:{}, children:[{ vIf:'ok', type:'b', children:['内容'] }] }`，生成 JS 代码字符串：① 条件节点编译为 `createIf(() => ctx.ok, () => [分支构建代码])`；② 非条件节点递归生成 `h()`/`template()` 调用；③ v-else 分支支持（else 分支生成 elseFn）；④ 生成代码可 eval 执行验证；⑤ vIf 嵌套正确处理。

**答**：

```javascript
export function compileIf(node, indent = '  ') {
  if (typeof node === 'string') return JSON.stringify(node);
  const kids = (node.children ?? [])
    .map((c) => c.vIf ? genIf(c, indent + '  ') : `h(${genNode(c, indent + '  ')})`);
  const kidCode = kids.length ? `, [${kids.join(', ')}]` : '';
  return `h(${JSON.stringify(node.type)}, ${JSON.stringify(node.props ?? {})}${kidCode})`;
}

function genIf(node, indent) {
  const branches = [[node.vIf, node]];
  let sib = node.next;                       // 相邻兄弟含 v-else
  while (sib?.vElse) { branches.push([sib.vIf ?? 'true', sib]); sib = sib.next; }
  const mk = (n) => `() => [${compileIf(n, indent + '    ')}]`;
  const cases = branches.map(([cond, n], i) =>
    i === 0 ? `cond(() => ctx.${cond}, ${mk(n)})`
            : `elseIf(() => ctx.${cond === 'true' ? 'true' : cond}, ${mk(n)})`);
  return `${indent}createIf(${cases.join(', ')})`;
}

// 生成的运行时代码（示意）：
// h('div', {}, [createIf(cond(() => ctx.ok, () => [h('b', {}, ['内容'])]))])
// createIf 实现：cond 为真 → 渲染 fn() 并挂载；变假 → 卸载；支持嵌套（fn 内再含 createIf）

// 验证：eval 生成代码 + ctx={ok:true} → DOM 包含 <b>内容</b>；ctx={ok:false} → 空
```

**评分点**：
- 递归代码生成结构清晰（genNode/genIf 分离，indent 处理）。
- v-else 链式分支收集正确（沿兄弟节点扫 elseIf）。
- createIf 运行时语义：真挂载/假卸载/嵌套分支递归。
- 生成代码可执行验证（编译器正确性的测试口径）。
