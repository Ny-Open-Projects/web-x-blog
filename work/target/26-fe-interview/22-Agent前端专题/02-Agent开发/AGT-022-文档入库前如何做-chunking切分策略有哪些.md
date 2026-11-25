---
title: [AGT-022] 文档入库前如何做 chunking？切分策略有哪些坑？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-022：文档入库前如何做 chunking？切分策略有哪些坑？
**答**：
- 目标：每个 chunk 语义完整且大小适中（常见 300~800 token），太碎丢失上下文、太大检索不精准。
- 优先按语义边界切：markdown 标题、段落、句子；超长段落再用滑动窗口，并保留 10%~20% overlap 防止语义被切断。
- 每块保留元数据（来源、标题层级），检索命中后能溯源（见 AGT-039）。
- 表格、代码块不要从中间切断；生产可用 LangChain 的 RecursiveCharacterTextSplitter。

```typescript
import fs from 'node:fs';

// 两级切分：先按 markdown 标题分段，超长段落再用滑动窗口 + overlap 兜底
function chunkDocument(doc: string, maxLen = 500, overlap = 50): string[] {
  const sections = doc.split(/\n(?=#{1,3}\s)/g); // 按标题切
  const chunks: string[] = [];

  for (const section of sections) {
    if (section.length <= maxLen) {
      chunks.push(section.trim());
      continue;
    }
    for (let i = 0; i < section.length; i += maxLen - overlap) {
      chunks.push(section.slice(i, i + maxLen).trim());
    }
  }
  return chunks.filter(Boolean);
}

const chunks = chunkDocument(fs.readFileSync('docs/react.md', 'utf-8'));
console.log(`共切出 ${chunks.length} 个 chunk`);
```
