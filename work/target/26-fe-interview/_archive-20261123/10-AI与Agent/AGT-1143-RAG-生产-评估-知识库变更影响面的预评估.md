---
title: [1143] 改知识库（下线文档/重构分块）之前，怎么预评估影响面
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 变更管理]
type: 面试题
---

## 1143：改知识库（下线文档/重构分块）之前，怎么预评估影响面

**答**：
- 影响面三问：哪些评估集条目的证据来自将变更的文档（直接受影响）、哪些高频 query 依赖它们（流量影响）、变更是「删除」还是「替换」（删除必查替代文档是否存在）。
- 预评估流程：变更申请 → 影响清单（评估条目 + query 覆盖）→ 评审（替代方案/时间窗口）→ 执行 → 回归验证（受影响条目必须复测）。
- 高危动作「下线文档」要软删除：先标记 deprecated（检索降权但不消失），观察两周无引用再物理删除——给未知依赖留缓冲。
- 追问钩子：为什么「引用计数」不够？——显式引用（其他文档链接）能计数，但 query 层的隐性依赖（用户天天问的问题靠这篇文档回答）只有 query 日志能发现，两者都要查。

```ts
async function preAssess(change) {
  const evalImpact = evalSet.filter(c => c.evidence.some(e => change.docs.has(e)));
  const queryImpact = await queryLog.topQueries({ docs: change.docs, days: 30 });
  if (change.type === 'delete' && !change.replacements.length) {
    return block('删除文档无替代，先补 replacements');
  }
  return plan({ evalImpact: evalImpact.length, queryImpact, window: 'low-peak' });
}
```
