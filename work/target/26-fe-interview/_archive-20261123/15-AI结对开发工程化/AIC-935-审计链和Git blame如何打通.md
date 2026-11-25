---
title: [AIC-935] 如何把 AI 产出审计链和 Git blame / commit 历史打通，让「这行代码谁写的」升级为「哪个 AI 决策写的」？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-935：如何把 AI 产出审计链和 Git blame / commit 历史打通，让「这行代码谁写的」升级为「哪个 AI 决策写的」？
**答**：
- 在 commit message/trailer 里嵌入审计链锚点（如 `AI-Session: s-1024`、`AI-Round: 7`、`AI-Prompt-Version: p13`），让 Git 记录与审计系统建立可跳转的引用。
- blame 某行时，若该行来自 AI 生成块，工具能根据文件 manifest 定位到对应会话轮次，展示「人发起 + AI 生成 + 人采纳」的完整责任链。
- 关键价值是「责任不缺位」：出问题既不能甩锅 AI（人是采纳者），也不能把 AI 产出当人写的——结论：打通后责任清晰到具体决策而非笼统的人。
- 追问钩子：能提出「审计锚点要随每次 commit 自动注入（通过 pre-commit 钩子），而非靠人手动填」的候选人懂落地细节。

```typescript
// commit trailer 嵌入审计锚点，打通 Git 与审计链
function buildCommitTrailer(manifest, filePath, lines) {
  const src = manifest.lines.find(l => l.file===filePath && lines[0]>=l.from && lines[0]<=l.to);
  if (!src) return '';
  return ['', `AI-Session: ${src.session}`, `AI-Round: ${src.round}`,
    `AI-Prompt-Version: ${src.promptVersion}`, `AI-Model: ${src.model}`].join('\n');
}
const msg = 'fix: 修正商品价格计算' + buildCommitTrailer(
  { lines:[{ file:'price.ts', from:10, to:20, session:'s-9', round:3, promptVersion:'p7', model:'gpt-x@v2' }] },
  'price.ts', [12]);
console.log(msg);
// git blame → 读 trailer → 跳转到审计系统对应会话轮次
```
