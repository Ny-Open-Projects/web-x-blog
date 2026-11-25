---
title: [AIC-039] 用 AI 生成 commit message 和 PR 描述的正确姿势是什么？为什么不能一键直提？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-039：用 AI 生成 commit message 和 PR 描述的正确姿势是什么？为什么不能一键直提？
**答**：
- 正确姿势：喂给 AI 完整 diff（不是文件名）+ 关联 issue + 本次意图说明，让它按团队规范（Conventional Commits）产出候选，人**确认语义后再提交**。
- 不能一键直提的原因：AI 只看得见 diff 看不见动机——它会把「临时调试代码」写成「增加调试能力」，语义失真的 commit 是考古毒药。
- 提示词要点：要求「why 优先」（一行动机 + body 说改动理由与影响面），禁止罗列文件清单凑字数；大 diff 按模块分组描述。
- 团队配套：commit 模板进 AI 规则文件；hook 层做格式校验（type/scope/subject 长度），AI 写得不合规直接打回。
- 追问钩子：PR 描述要加「风险与回滚」段——这是 AI 最容易漏、reviewer 最关心的部分，模板里显式留槽位。

```javascript
// commit message 生成 prompt + 格式校验
const commitPrompt = `
根据 diff 与意图生成 commit message：
- 格式：<type>(<scope>): <subject>，subject ≤ 50 字符
- body 说明动机与影响面（why 优先，不要罗列文件名）
- 风险点单独一行 RISK:
意图：${intent}
<diff>${diff}</diff>`;
function validateCommit(msg) {
  return /^(feat|fix|refactor|chore|test|docs|perf)\([\w-]+(\([\w-]+\))?\): .{1,50}$/.test(msg.split('\n')[0])
    ? { ok: true } : { ok: false, reason: '不符合 Conventional Commits 或 subject 过长' };
}
```
