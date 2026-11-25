---
title: [1133] 用户凭什么信任一条多 Agent 链路的结果
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 信任]
type: 面试题
---

## 1133：用户凭什么信任一条多 Agent 链路的结果

**答**：
- 信任三支柱：可验证（关键结论带引用/可点击溯源）、一致性（同类问题答案稳定，不自相矛盾）、可纠正（用户指出错误后能修正且记住修正）——三者缺一，用户很快弃用。
- 「过程可见」的度：给用户看「步骤摘要」（检索了什么、参考了什么）建立理解，但不暴露内部 Agent 名与技术细节（用户不关心 coder-1 还是 coder-2）。
- 信任破坏的恢复：出错后的响应比不出错更影响长期信任——明确承认 + 修正 + 说明防复发，比装作没事强得多。
- 追问钩子：什么设计会摧毁信任？——悄悄降级（答案质量突变无提示）、答案模棱两可不表态、引用点开 404（溯源是假的）。

```ts
function answerCard(result) {
  return {
    summary: result.answer,
    sources: result.citations.map(c => ({ label: c.title, url: c.link })), // 可点击
    process: '参考了 3 个知识库 12 篇文档',      // 步骤摘要，非技术细节
    degraded: result.level !== 'confident' ? '精简模式结果' : null, // 降级透明
  };
}
```

