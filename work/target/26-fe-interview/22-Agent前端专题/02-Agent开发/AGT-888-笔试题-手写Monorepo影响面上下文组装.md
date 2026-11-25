---
title: [AGT-888] 手写 buildContext：依赖图affected、分层加载（根/接口/全文）、预算裁剪？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-888：手写 buildContext：依赖图affected、分层加载（根/接口/全文）、预算裁剪

**需求与边界**：
- 实现 buildContext(task, repo, budget)。
- 边界要求：① affected = 依赖图中直接依赖受改文件的包（闭包）；② 三层内容：根 ARCHITECTURE.md 全文 → affected 包接口签名 → 目标文件全文；③ 超预算裁剪顺序：先裁接口层（远端包优先），根文档与目标文件不裁；④ 返回 { parts, usedTokens }。

**答**：
```javascript
function buildContext(task, repo, budget) {
  const affected = repo.depGraph.affectedOf(task.files); // 闭包
  const targetTokens = sumTokens(task.files.map(f => f.content));
  const rootTokens = tokenCount(repo.root('ARCHITECTURE.md'));
  let remaining = budget - targetTokens - rootTokens;
  const ifaces = affected
    .sort((a, b) => dist(a, task.files) - dist(b, task.files)) // 近端优先
    .map(p => ({ pkg: p, text: repo.interfaces(p),
      tokens: tokenCount(repo.interfaces(p)) }));
  const kept = [];
  for (const it of ifaces) {                       // 远端先裁
    if (remaining - it.tokens < 0) continue;
    remaining -= it.tokens; kept.push(it);
  }
  return { parts: [
    { layer: 'root', text: repo.root('ARCHITECTURE.md') },
    ...kept.map(k => ({ layer: 'interface', ...k })),
    ...task.files.map(f => ({ layer: 'target', text: f.content })),
  ], usedTokens: budget - remaining };
}
```

**评分点**:
- 影响面闭包计算正确；三层分层加载（根约束/接口/全文）。
- 裁剪顺序明确（远端接口先裁），根文档与目标文件保底（核心上下文不丢）。
- usedTokens 记账（预算可核算）。

