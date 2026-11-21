---
title: [AIC-046] AI 审查大 PR 时「只看 diff」会漏什么？增量审查怎么补全上下文？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-046：AI 审查大 PR 时「只看 diff」会漏什么？增量审查怎么补全上下文？
**答**：
- 只看 diff 的典型漏报：调用方被改了签名但调用点没同步（调用点在 diff 外）、删除了仍被引用的工具函数、常量改动影响了另一模块的假设、样式类名冲突。
- 补全策略：以 diff 涉及文件为中心，收集「双向关联」——它 import 的（依赖）和 import 它的（调用方），调用方给签名层即可。
- 大 PR 拆分审查：按模块分组分别调用（每组带上该组完整文件），再汇总一轮「跨组一致性检查」（签名对齐、命名统一）。
- 预算控制：上下文不够时优先保「调用方签名 + 被改函数全文」，牺牲与本 diff 无关部分。
- 追问钩子：这正是笔试题 AIC-147 diff 审查器的原型——把「收集 diff→扩上下文→分组→汇总」工程化。

```javascript
// 增量审查上下文构建：diff + 双向关联
function buildReviewContext(diff, repo) {
  const files = [...new Set([...diff.matchAll(/^diff --git a\/(.+?) b\//gm)].map(m => m[1]))];
  const ctx = [];
  for (const f of files) {
    ctx.push({ file: f, content: repo.read(f), reason: 'changed' });
    for (const importer of repo.findImporters(f)) {
      ctx.push({ file: importer, content: repo.signatures(importer), reason: 'caller' }); // 调用方签名层
    }
  }
  return ctx;
}
```
