---
title: [AGT-865] 生产问题让 AI 调试（例如这个报错帮我看看），有效调试的上下文要包含什么？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-865：生产问题让 AI 调试（例如这个报错帮我看看），有效调试的上下文要包含什么

**答**：
- 调试上下文四要素：错误现场（报错+堆栈+sourcemap 还原）、运行环境（浏览器/版本/构建产物 hash）、复现路径（用户操作序列/录屏）、代码上下文（相关组件与依赖链）。缺现场信息的 AI 调试就是瞎猜——先自动采集再问 AI。
- 调试协议：AI 先给「假设清单+每个假设的验证方法」，人执行验证回填结果，多轮收敛——而不是让 AI 一次给答案（容易一本正经地错）。
- 会话化：调试上下文（假设/验证结果）持久化成调试记录，同类问题检索复用。

```javascript
async function aiDebug(issue) {
  const ctx = await collect({
    error: issue, env: issue.userAgent, build: issue.buildHash,
    replay: issue.userActions, code: loadRelated(issue.stack),
  });
  return llm.debug(ctx, { protocol: 'hypothesis-loop',
    require: '每个假设附验证方法',                 // 协议约束
    forbid: '不确定时明确说不知道' });
}
```

