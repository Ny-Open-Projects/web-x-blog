---
title: [AIC-845] IDE 里的采纳数据和 CI 里的质量数据，怎么关联到同一次开发活动？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-845：IDE 里的采纳数据和 CI 里的质量数据，怎么关联到同一次开发活动？
**答**：
- 难点在于两侧数据天然割裂：IDE 事件是「会话维度、匿名、高频」，CI 数据是「提交/PR 维度、有身份、低频」。需要一个**共同的关联键**。
- 推荐用**工作区/分支 + 提交哈希**做桥梁：IDE 插件在生成代码时把 `sessionId` 写入本地元数据；开发者提交时，hook 把最近会话的 `sessionId` 列表写进 commit message trailer（如 `AI-Session: abc,def`）；CI 解析 commit 拿到 sessionId，就能把「这次提交里用了哪些 AI 建议」和「CI 质量结果」串起来。
- 更稳妥的做法是用**内容指纹**：对采纳的代码片段做哈希，CI 时在 diff 里匹配指纹，即使 sessionId 丢失也能关联（但成本高、有误匹配）。
- 隐私：关联用匿名 sessionId，身份映射表单独加密存储且严格授权；分析默认在团队聚合层，个人级只反馈给本人。
- 追问钩子：能说出「用 commit trailer 携带 AI 会话元数据」的候选人，给出了一个低成本、可审计的工程解法，而不是空谈「建数据中台」。

```typescript
// IDE 侧：提交 hook 把会话 ID 写进 commit trailer
function buildCommitMessage(msg: string, sessionIds: string[]) {
  if (!sessionIds.length) return msg;
  return `${msg}\n\nAI-Session: ${[...new Set(sessionIds)].join(',')}`;
}

// CI 侧：解析 commit，把质量结果与 AI 会话关联
function linkCI(commitMsg: string, quality: { bugs: number; passed: boolean }) {
  const m = commitMsg.match(/^AI-Session:\s*(.+)$/m);
  const sessions = m ? m[1].split(',').map(s => s.trim()) : [];
  return sessions.map(sessionId => ({
    sessionId,
    ciBugCount: quality.bugs,
    ciPassed: quality.passed,
    // 现在可以回答："用了 AI 建议的那些提交，质量如何？"
  }));
}
const msg = buildCommitMessage('feat: 支付页重构', ['anon-a', 'anon-b']);
console.log(linkCI(msg, { bugs: 0, passed: true }));
// [{ sessionId:'anon-a', ... }, { sessionId:'anon-b', ... }]
```
