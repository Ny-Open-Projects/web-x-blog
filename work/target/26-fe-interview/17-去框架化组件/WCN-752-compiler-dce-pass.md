---
title: [WCN-752] 笔试：手写基于常量条件的死代码消除 pass
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-752：笔试：手写基于常量条件的死代码消除 pass

**答**：
- 需求：实现 `dce(nodes, env)`，nodes 为 AST 节点数组，节点形如 `{ type:'El'|'If'|'Text', test?, children? }`。If 节点若 test 是常量（`true/false` 布尔或 `'prod'/'dev'` 字符串，可用 env 解析），用 env 求值后保留对应分支（children），否则保留 If 本身并递归处理 children。返回精简后的节点数组。
- 要点：常量判定用 env 映射 + 字面量布尔；保留分支时把分支 children 展开到结果；边界：空 children、未知常量保留原节点。

```javascript
function dce(nodes, env = {}) {
  const out = [];
  for (const n of nodes || []) {
    if (n.type === 'If') {
      const t = n.test;
      let known = typeof t === 'boolean' ? t : (t in env ? env[t] === 'prod' : null);
      if (known === true) out.push(...dce(n.children, env));       // 保留 then 分支
      else if (known === false) { /* 删除 */ }
      else out.push({ ...n, children: dce(n.children, env) });      // 未知，递归保留
    } else if (n.children) {
      out.push({ ...n, children: dce(n.children, env) });
    } else {
      out.push(n);
    }
  }
  return out;
}
console.log(dce([
  { type: 'If', test: false, children: [{ type: 'El', name: 'dev' }] },
  { type: 'If', test: 'env', children: [{ type: 'El', name: 'prod' }] },
], { env: 'prod' }));
```

**评分点**：
- 常量条件（布尔/env 映射）正确求值并剪枝。
- 保留分支时把 children 展开合并到输出，结构正确。
- 未知条件递归保留而非误删，安全保守。
- 空数组/缺字段有边界防御。
