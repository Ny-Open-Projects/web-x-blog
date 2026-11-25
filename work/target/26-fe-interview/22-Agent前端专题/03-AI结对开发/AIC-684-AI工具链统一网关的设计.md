---
title: [AIC-684] 团队 AI 统一网关要承担哪些职责？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-684：团队 AI 统一网关要承担哪些职责？

**答**：
- 结论先行：**网关是所有 AI 调用的「单一入口」，承担鉴权、路由、计量、审计、限流、脱敏六大职责**——把这些横切关注点收敛到一处，是平台化的第一步（AIC-118 网关职责 / AIC-275 团队级网关）。
- 六大职责：1) **鉴权**：统一身份与权限，谁能用哪些模型/能力；密钥不散落在每人机器上；2) **路由**：按任务/成本/隐私/健康度选模型（AIC-683）；3) **计量**：记录 token 消耗，按团队/项目分摊成本（AIC-172 计费 / AIC-119 分摊）；4) **审计**：记录所有调用（谁、何时、什么内容、什么结果），供合规与事故追溯（AIC-456 审计日志）；5) **限流**：令牌桶防风暴、配额防超支（AIC-174）；6) **脱敏**：敏感数据出网前脱敏（AIC-321）。
- 额外价值：1) **可观测性**——所有调用集中，容易做监控与告警（AIC-085）；2) **解耦**——上层工具不绑定具体模型，换模型只改网关配置（AIC-290 防锁定）；3) **灰度**——新模型/新 prompt 在网关层灰度（AIC-696）。
- 追问钩子：为什么「密钥集中到网关」是安全收益而非风险？——因为密钥散落在 N 个开发者机器上，泄露面是 N；集中到网关后泄露面是 1，且网关可以做审计和最小权限；「单点」在这里是「单一可控点」，比「多点失控」安全得多。

```typescript
// 网关请求处理流水线：横切关注点集中在单一入口
type Req = { user: string; team: string; tokens: number; sensitivity: string; content: string };

function handleRequest(req: Req, ctx: {
  auth: (u: string) => boolean;
  sanitize: (c: string, level: string) => string;
  route: (level: string) => string;
  meter: (team: string, tokens: number) => void;
  audit: (e: any) => void;
  limit: (team: string) => boolean;
}) {
  if (!ctx.auth(req.user)) throw new Error('unauthorized');
  if (!ctx.limit(req.team)) throw new Error('rate-limited');
  const safeContent = ctx.sanitize(req.content, req.sensitivity);
  const model = ctx.route(req.sensitivity);
  ctx.meter(req.team, req.tokens);
  ctx.audit({ user: req.user, model, tokens: req.tokens, ts: Date.now() });
  return { model, content: safeContent }; // 调用具体模型...
}

const ctx = {
  auth: u => u === 'alice', limit: () => true,
  sanitize: (c: string) => c.replace(/token=\w+/g, 'token=***'),
  route: () => 'cloud-model', meter: () => {}, audit: () => {},
};
console.log(handleRequest({ user: 'alice', team: 'fe', tokens: 100, sensitivity: 'L2',
  content: 'req token=abc123' }, ctx).content.includes('***'));
```
