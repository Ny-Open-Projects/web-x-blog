---
title: [AIC-027] 如何让 AI 严格输出 JSON 等结构化结果？输出格式约束有哪些手段与兜底方案？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-027：如何让 AI 严格输出 JSON 等结构化结果？输出格式约束有哪些手段与兜底方案？
**答**：
- 手段按可靠性排序：API 的 structured output / JSON mode（服务端强制）> function calling / tool schema > prompt 里给 JSON Schema 示例 > 口头要求「输出 JSON」。
- prompt 层技巧：给出精确 schema、给一个填好的完整示例、明确「不要输出 markdown 代码围栏、不要解释文字」。
- 兜底必须做：解析失败后进入「修复循环」——把报错和原始输出回喂给模型让它自我修正，最多重试 2 次，仍失败则降级人工。
- 模型输出常见脏点：围栏包裹、尾随逗号、单引号、注释、截断的半截 JSON，解析器要做宽容处理。
- 追问钩子：温度调 0 + schema 约束双管齐下，能让结构化输出成功率到 99%+，但别忘了校验业务字段（不只是 JSON 合法）。

```javascript
// 结构化输出解析 + 修复循环兜底
function parseAiJson(text) {
  const cleaned = text.replace(/^```(json)?\s*|\s*```$/g, '').trim(); // 去围栏
  try { return { ok: true, data: JSON.parse(cleaned) }; }
  catch (e) { return { ok: false, error: e.message, raw: cleaned }; }
}
async function askStructured(prompt, schema, maxRetry = 2) {
  let messages = [{ role: 'user', content: `${prompt}\n严格按此 JSON Schema 输出，不要任何多余文字：${JSON.stringify(schema)}` }];
  for (let i = 0; i <= maxRetry; i++) {
    const res = await callLLM(messages, { temperature: 0 });
    const parsed = parseAiJson(res);
    if (parsed.ok) return parsed.data;
    messages.push({ role: 'assistant', content: res });
    messages.push({ role: 'user', content: `JSON 解析失败：${parsed.error}。请只输出修正后的完整 JSON。` });
  }
  throw new Error('structured output failed after retry');
}
```
