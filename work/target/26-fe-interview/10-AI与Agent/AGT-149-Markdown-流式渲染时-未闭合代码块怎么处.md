---
title: [AGT-149] Markdown 流式渲染时，未闭合代码块怎么处理？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-149：Markdown 流式渲染时，未闭合代码块怎么处理？
**答**：
- 问题：流式中途 ```` ``` ```` 只出现一半（开栅栏闭合前），常规 markdown 解析器会把代码内容当普通段落渲染，结束后又突变回代码块，视觉抖动严重。
- 两种策略：预处理补全（解析前检测未闭合栅栏并临时补上闭合标记，每帧都渲染「确定态」）、分段渲染（已完成块缓存为静态 HTML，只有最后一个未完成块走增量渲染）。
- 预处理还要处理：未闭合行内 ` `` `、未闭合表格行、列表悬挂项——原则是「给解析器喂合法的最小补全输入」。
- 性能要点：全文每 token 重新 parse 会卡，用「稳定前缀 + 活跃尾部」分区：块级完成即标记 immutable，解析只作用于尾部。

```typescript
// Markdown 流式渲染：栅栏补全 + 稳定前缀分区
function balanceFences(src: string): string {
  const fenceCount = (src.match(/^```/gm) ?? []).length;
  if (fenceCount % 2 === 1) src += '\n```';            // 奇数栅栏：补闭合
  if (/(`[^`\n]*)$/.test(src)) src += '`';             // 行内代码未闭合：补反引号
  return src;
}

export class StreamingMarkdown {
  private stableHtml = '';        // 已完成块的缓存 HTML
  private stableOffset = 0;

  render(fullText: string): { html: string; activeBlock: boolean } {
    const lastFenceEnd = findLastClosedBlock(fullText);
    if (lastFenceEnd > this.stableOffset) {
      // 块级完成：新完成的段落一次性解析进缓存（immutable）
      const donePart = fullText.slice(this.stableOffset, lastFenceEnd);
      this.stableHtml += window.markdownit().render(donePart);
      this.stableOffset = lastFenceEnd;
    }
    const tail = fullText.slice(this.stableOffset);
    const patched = balanceFences(tail);                // 活跃尾部：补全后再解析
    return { html: this.stableHtml + window.markdownit().render(patched), activeBlock: /^```/.test(tail) };
  }

  reset() { this.stableHtml = ''; this.stableOffset = 0; }
}

function findLastClosedBlock(text: string): number {
  const it = window.markdownit(); // 借助 token 遍历找最后一个完整块边界
  const tokens = it.parse(text, {});
  let mapEnd = 0;
  for (const t of tokens) {
    if (t.map && t.level === 0) mapEnd = Math.max(mapEnd, t.map[1]);
  }
  // 将行号转回字符偏移
  let offset = 0, line = 0;
  while (line < mapEnd && offset < text.length) offset = text.indexOf('\n', offset) + 1, line++;
  return offset;
}
```
