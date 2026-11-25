---
title: [AIC-933] IM 消息模块让 AI 生成端到端加密逻辑，如何满足安全团队的合规审计要求？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-933：IM 消息模块让 AI 生成端到端加密逻辑，如何满足安全团队的合规审计要求？
**答**：
- 加密/安全类代码是「高危区」——结论：AI 只能做脚手架与样板，密钥管理、随机数来源、协议细节必须由人设计并逐行评审，不能整体外包。
- 审计上要额外留痕：生成时记录「安全约束清单」（如禁止硬编码密钥、必须用 CSPRNG、前向保密），并让 AI 逐条声明如何满足；评审时按清单核对。
- 用「安全回归测试 + 静态分析」双门禁：AI 生成的加密代码必须通过已知向量测试（如标准算法测试向量）和密钥泄露扫描，才允许入库。
- 追问钩子：能明确说出「安全敏感模块的 AI 产出边界——可辅助不可主导，人承担最终责任」的候选人，具备风险分级意识。

```typescript
// 安全约束清单：AI 生成加密代码时逐条核对
const securityChecks = [
  { rule:'无硬编码密钥', test:src => !/(secret|key)\s*=\s*['"][A-Za-z0-9]{8,}/i.test(src) },
  { rule:'使用安全随机源', test:src => /crypto\.getRandomValues|randomBytes/.test(src) },
  { rule:'标准算法已知向量', test:src => runKnownVector(src) },
];
function runKnownVector(src){ return /aes|sha-?256/i.test(src); } // 示意：实际跑标准测试向量
function gate(src) {
  return securityChecks.filter(c => !c.test(src)).map(c => c.rule);
}
console.log('未满足的安全约束:', gate('const k = crypto.getRandomValues(new Uint8Array(16))'));
```
