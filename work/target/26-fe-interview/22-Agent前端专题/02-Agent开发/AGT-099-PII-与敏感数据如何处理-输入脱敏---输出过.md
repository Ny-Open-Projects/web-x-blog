---
title: [AGT-099] PII 与敏感数据如何处理（输入脱敏 / 输出过滤）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-099：PII 与敏感数据如何处理（输入脱敏 / 输出过滤）？
**答**：
- 两个方向：输入脱敏（发给第三方模型前把手机号/身份证/邮箱替换为占位符，本地保留映射）、输出过滤（占位符还原或意外泄露拦截）。
- 可逆脱敏：会话内维护「占位符 → 原文」映射，模型输出里的占位符还原成真实值返回给用户本人——数据出了境但形态安全。
- 检测分层：正则（手机号/身份证等强模式）先行，NER 模型兜底（姓名/地址等弱模式）；拿不准的宁可脱敏。
- 日志同样要脱敏：审计与调试日志落库前统一过脱敏管道，否则等于白做。

```typescript
import { z } from 'zod';

// PII 检测与可逆脱敏
const PII_RULES: { type: string; re: RegExp }[] = [
  { type: 'PHONE', re: /1[3-9]\d{9}/g },
  { type: 'EMAIL', re: /[\w.+-]+@[\w-]+\.[\w.]+/g },
  { type: 'ID_CARD', re: /\d{17}[\dXx]/g },
];

export function maskPII(text: string) {
  const map = new Map<string, string>();
  let masked = text;
  for (const { type, re } of PII_RULES) {
    masked = masked.replace(re, (m) => {
      const ph = `__${type}_${map.size}__`;
      map.set(ph, m);                              // 占位符 → 原文，会话内可还原
      return ph;
    });
  }
  return { masked, map };
}

export const unmaskPII = (text: string, map: Map<string, string>) =>
  text.replace(/__\w+_\d+__/g, (ph) => map.get(ph) ?? ph);

// 网关集成：入站脱敏 → LLM → 出站还原
export async function maskedChat(messages: ChatMessage[]) {
  const last = messages.at(-1)!;
  const { masked, map } = maskPII(last.content);
  const safeMessages = [...messages.slice(0, -1), { ...last, content: masked }];
  const output = await chatOnce(safeMessages);
  return unmaskPII(output, map);                   // 还原给用户本人；发给模型的版本已脱敏
}
// 日志管道统一走 maskPII：审计与调试日志中永不出现原始 PII
```
