---
title: [AGT-131] 长文档超出上下文的处理策略有哪些？map-reduce 分段摘要怎么实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-131：长文档超出上下文的处理策略有哪些？map-reduce 分段摘要怎么实现？
**答**：
- 三类策略：滑动窗口（线性读，适合找局部答案）、map-reduce 分段摘要（全局理解：每段独立摘要再汇总）、迭代 refine（逐段把上一段摘要带进来滚动精炼，全局一致性更好但串行慢）。
- 选择依据：问答定位类用检索（先 chunk 向量化，只取相关段）；全文分析/报告生成用 map-reduce；需要上下文连贯的叙事理解用 refine。
- map 阶段必须并行（Promise.all）才有工程价值；chunk 切分要带重叠，避免句子被拦腰截断导致摘要丢义。
- reduce 阶段的输出要控制长度：限制每段摘要 token 数，防止 reduce 输入又超限需要二次归并。

```typescript
// 长文档三种处理策略实现
const CHUNK_SIZE = 3000, OVERLAP = 200;

function chunkText(text: string): string[] {
  const chunks: string[] = [];
  for (let i = 0; i < text.length; i += CHUNK_SIZE - OVERLAP) {
    chunks.push(text.slice(i, i + CHUNK_SIZE));
    if (i + CHUNK_SIZE >= text.length) break;
  }
  return chunks;
}

export async function mapReduceSummarize(doc: string, llm: (p: string) => Promise<string>): Promise<string> {
  // map：并行摘要每段，并限制单段摘要长度
  const chunkSummaries = await Promise.all(
    chunkText(doc).map((c) => llm(`用不超过 200 字概括以下内容，保留关键数字与结论：\n${c}`)),
  );
  // reduce：摘要仍然过长则递归归并
  let merged = chunkSummaries.join('\n\n');
  while (merged.length > CHUNK_SIZE * 2) {
    const parts = chunkText(merged);
    merged = (await Promise.all(parts.map((p) => llm(`合并概括：\n${p}`)))).join('\n\n');
  }
  return llm(`基于以下分段摘要，输出全文的综合总结：\n${merged}`);
}

export async function refineSummarize(doc: string, llm: (p: string) => Promise<string>): Promise<string> {
  let acc = '';
  for (const c of chunkText(doc)) {              // 串行：每段携带前文摘要
    acc = await llm(`已有摘要：${acc || '无'}\n请结合下一段更新摘要：\n${c}`);
  }
  return acc;
}

// 滑动窗口问答：窗口内找不到答案则滑动，适合定位类问题
export async function slidingQa(doc: string, question: string, llm: (p: string) => Promise<string>): Promise<string> {
  for (const c of chunkText(doc)) {
    const ans = await llm(`仅当以下文本包含答案时回答，否则回答「未找到」：\n问题：${question}\n文本：${c}`);
    if (!ans.includes('未找到')) return ans;
  }
  throw new Error('全文窗口均未命中，建议改用检索策略');
}
```
