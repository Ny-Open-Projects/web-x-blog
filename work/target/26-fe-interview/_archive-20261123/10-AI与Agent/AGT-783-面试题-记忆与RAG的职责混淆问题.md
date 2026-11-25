---
title: [AGT-783] 用户的偏好和知识库里的规范冲突时怎么办，记忆与 RAG 的职责边界？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-783：用户的偏好和知识库里的规范冲突时怎么办，记忆与 RAG 的职责边界

**答**：
- 职责分界：记忆=「关于这个用户的事实与偏好」，RAG=「世界的客观知识与企业规范」；用户偏好可以让回答换表达，但不能推翻规范（用户说"不用写测试"不覆盖团队规范的测试要求）。
- 冲突处理顺序：企业规范 > 用户偏好；冲突时执行规范并说明原因（"团队规范要求测试，我仍会生成测试；你的偏好已记录，对个人项目生效"）。
- 检测机制：注入时比对记忆与 RAG 命中的语义冲突，高冲突注入让模型显式声明而不是默默选一边。

```javascript
function detectConflict(mem, rag) {
  return mem.facts.filter(m =>
    rag.docs.some(d => contradicts(m.statement, d.claim)))
    .map(m => ({ memory: m, rag: contradicter, rule: 'norm-over-pref' }));
}
function injectWithConflict(ctx) {
  if (ctx.conflicts.length)
    ctx.system += '存在用户偏好与规范的冲突：以规范为准，回答中说明原因。';
  return ctx;
}
```

