---
title: [PER-193] AI 助手生成代码如何审计？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-193：AI 助手生成代码如何审计？

**答**：
- AI 代码的高频风险模式：模板串直接进 innerHTML、eval/new Function、敏感数据进 localStorage、`Math.random` 当安全随机数、编造不存在的 API（幻觉依赖）。
- 工程动作：pre-commit 钩子集中拦截高危模式；PR 标注 `ai-assisted` 的**强制双人评审**；幻觉依赖靠 lockfile diff + 依赖白名单拦截。
- 制度配套：AI 生成比例进 CR 标签统计，AI 相关事故进复盘模板单独归类，持续迭代拦截规则。
- 底线认知：AI 是加速器不是审批人——生成代码与手写代码承担完全相同的门禁与评审标准。

```javascript
// AI 生成代码审计门禁：pre-commit 对高危模式集中拦截
// package.json: { "lint-staged": { "*.{js,ts,jsx,tsx,vue}": ["node scripts/ai-code-audit.js"] } }
import { readFileSync } from 'node:fs';

const RISKY = [
  [/innerHTML\s*=\s*[`"'][^`"']*\$\{/, 'AI 常见：模板串直接进 innerHTML，需改 DOMPurify.sanitize'],
  [/eval\(|new Function\(/, '禁止动态执行'],
  [/localStorage\.setItem\([^)]*(token|secret|password)/i, '敏感数据不得进 localStorage'],
  [/Math\.random\(\)[^\n]*(token|nonce|secret)/i, '安全随机数必须用 crypto.getRandomValues'],
  [/(require|import)\s*\(?\s*[`"'][^`"']*(gpt|copilot|magic)-?[a-z]*[`"']/i, '幻觉依赖检查：确认该包真实存在'],
];

let fail = false;
for (const f of process.argv.slice(2)) {
  const src = readFileSync(f, 'utf8');
  RISKY.forEach(([re, msg]) => {
    if (re.test(src)) { console.error(`${f}: ${msg}`); fail = true; }
  });
}
process.exit(fail ? 1 : 0);
// 配套制度：PR 标注 ai-assisted 的强制双人评审
```
