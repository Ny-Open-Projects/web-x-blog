---
title: [AIC-061] 用 AI 从 commit 历史生成 changelog 和版本说明怎么做？怎么保证不漏不编？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-061：用 AI 从 commit 历史生成 changelog 和版本说明怎么做？怎么保证不漏不编？
**答**：
- 流程：确定性工具收集区间内 commit（git log + conventional commit 解析分组）→ AI 只负责「把技术描述翻译成用户视角的版本说明」→ 人工审阅后发布。
- 不漏：commit 清单是输入而不是 AI 自己去想，漏项只可能是解析漏（规范外的 commit），所以 commit 规范是前置条件（呼应 AIC-039）。
- 不编：约束 AI「每个条目必须能对应到 commit hash」，输出带 hash 引用；校验器检查引用的 hash 是否都存在于输入清单。
- 结构化输出：Features/Fixes/Breaking 三段，Breaking 必须含迁移指引——AI 对 breaking 的敏感度要在 prompt 里显式强调。
- 追问钩子：用户视角翻译容易过度营销化（"革命性优化"），约束「动词具体、禁止形容词堆砌」。

```javascript
// changelog 生成 + 引用校验
async function generateChangelog(commits) {
  const input = commits.map(c => `${c.hash} ${c.type}: ${c.subject}`).join('\n');
  const text = await callLLM(`根据 commit 清单生成版本说明（Features/Fixes/Breaking 三段，每条末尾附 hash，禁止形容词堆砌）：\n${input}`);
  const refs = [...text.matchAll(/\b([0-9a-f]{7,10})\b/g)].map(m => m[1]);
  const valid = new Set(commits.map(c => c.hash.slice(0, 10)));
  const phantom = refs.filter(h => !valid.has(h.slice(0, 10)));
  if (phantom.length) throw new Error(`changelog 引用了不存在的 commit: ${phantom}`);
  return text;
}
```
