---
title: [AIC-970] IM 项目多个小组各有一套 AI 规范（命名/测试/提交都不同），如何收敛又不过度中央集权？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-970：IM 项目多个小组各有一套 AI 规范（命名/测试/提交都不同），如何收敛又不过度中央集权？
**答**：
- 先「分类」规范：全局强规范（安全、合规、核心接口约定）必须统一；局部习惯（命名风格、目录组织）允许各组保留——结论：分层治理而非一刀切。
- 用「分层继承」组织 rules：仓库根是全局底线，各组目录有局部 rules 继承并覆盖可覆盖项；工具支持优先级解析（呼应 AIC-012/207 但换视角在收敛治理）。
- 收敛靠「演进」而非「革命」：先统一分歧最大、收益最高的几条（如提交规范），定期收集各组反馈逐步对齐；强推全部统一常引发抵触。
- 追问钩子：能提出「设一个跨组规范委员会，规范变更走 RFC + 投票，让收敛有合法性与参与感」的候选人懂大规模团队的治理机制。

```typescript
// 分层规范：全局底线 + 局部覆盖
const rules = {
  global: { security:'禁止硬编码密钥', commit:'conventional commits' },
  groups: {
    imCore: { extends:'global', naming:'camelCase' },
    imUI:   { extends:'global', naming:'kebab-case' }, // 局部可不同
  },
};
function resolveRule(group, key) {
  const g = rules.groups[group];
  return g?.[key] ?? rules.global[key] ?? null;
}
console.log(resolveRule('imUI','naming'), resolveRule('imUI','security'));
// 强规范(security)统一，局部习惯(naming)各组自治
```
