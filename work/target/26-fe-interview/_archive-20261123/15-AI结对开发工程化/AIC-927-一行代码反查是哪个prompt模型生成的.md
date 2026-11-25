---
title: [AIC-927] 商品列表上线后出问题，如何从一行可疑代码反查它是哪个 prompt、哪个模型、第几轮生成的？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-927：商品列表上线后出问题，如何从一行可疑代码反查它是哪个 prompt、哪个模型、第几轮生成的？
**答**：
- 前提是「产出即带元数据」：每次 AI 生成的代码在提交时携带溯源信息（prompt 版本、模型版本、会话 ID、轮次、生成时间），以 commit trailer 或独立 manifest 文件形式入库。
- 反查链路：代码行 → 所在文件的生成记录（manifest）→ 会话与轮次 → 当时的 prompt 与上下文快照 → 责任上下文。没有这一步，反查只能靠翻聊天记录，不可靠。
- 要有「快照可回放」能力：保存的上下文快照能重新喂给当时版本的模型，复现生成过程——结论：可追溯不仅是记录，还要能回放验证。
- 追问钩子：能强调「溯源元数据必须随代码同 commit 入库、与代码同生命周期，否则一旦聊天记录丢失就断链」的候选人懂审计链的完整性与不可抵赖。

```typescript
// 产出溯源 manifest（随 commit 入库）
const manifest = {
  file:'src/ProductList.tsx',
  lines:[{ from:42, to:58, session:'s-1024', round:7,
    model:'gpt-x@2026-11-01', promptVersion:'p-v13', generatedAt:'2026-11-23T10:00:00Z' }],
};
function traceLine(manifest, lineNo) {
  return manifest.lines.find(l => lineNo >= l.from && lineNo <= l.to) ?? null;
}
console.log(traceLine(manifest, 50)); // 反查到 s-1024 会话第7轮、模型版本与 prompt 版本
// 配合快照可回放：取出当时上下文 + 模型版本 → 重新生成验证
```
