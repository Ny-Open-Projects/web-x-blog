---
title: [SCN-1223] AI 对话的语气/角色设定（Persona 管理）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1223：AI 对话的语气/角色设定（Persona 管理）

**答**：
- 设定：系统角色设定（"你是资深前端"）预置 Persona 库，用户自定义。
- 隔离：Persona 只影响 system prompt（不改模型参数），会话级生效。
- 合规：角色设定不得绕过安全策略（系统安全 prompt 优先级最高）。

```javascript
// Persona 管理
const PERSONAS = {
  senior_fe: '你是资深前端工程师，回答注重工程实践与权衡。',
  teacher: '你是耐心的老师，用类比解释概念。',
};
function buildSystemPrompt(personaId, userCustom) {
  const safety = SAFETY_PROMPT;                      // 安全策略最高优先
  const persona = PERSONAS[personaId] ?? userCustom ?? '';
  return [safety, persona].filter(Boolean).join('\n');
}
const SAFETY_PROMPT = '遵守内容安全规范，拒绝违法有害请求。';
```
