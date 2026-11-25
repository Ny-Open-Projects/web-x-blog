---
title: [AIC-171] 笔试：实现一个语义 chunk 切分器：按结构边界（函数/标题）优先、超长回退滑窗、保留重叠上下文？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-171：笔试：实现一个语义 chunk 切分器：按结构边界（函数/标题）优先、超长回退滑窗、保留重叠上下文？
**需求**：实现 `chunk(text, { maxTokens, overlap })`：
- 优先按结构边界切：markdown 标题（/^#{1,3}\s/）、代码块、函数定义行；
- 单个结构内超 maxTokens 时回退滑窗（固定 token 窗口 + overlap 重叠）；
- 每个 chunk 带元信息 `{type, index}`；相邻 chunk 保留 overlap 行上下文；
- 目标：检索时每个 chunk 自足可读（含标题路径前缀）。

```javascript
function tokensOf(s) {
  const cjk = (s.match(/[\u4e00-\u9fa5]/g) || []).length;
  return Math.ceil(cjk / 1.5 + (s.length - cjk) / 4);
}
const FENCE = '\u0060'.repeat(3);   // 代码围栏（码点构造，避免源码内出现字面围栏）
const BOUNDARY = [/^#{1,3}\s/, /^export\s+(async\s+)?(function|class|const)\s/, new RegExp('^' + FENCE)];

function chunk(text, { maxTokens = 500, overlap = 2 } = {}) {
  const lines = text.split('\n');
  const chunks = [];
  let headingPath = '';
  let cur = [], curType = 'text', curTokens = 0;

  const flush = (index) => {
    if (!cur.length) return;
    const body = cur.join('\n');
    chunks.push({
      type: curType, index,
      tokens: curTokens,
      text: (headingPath ? `${headingPath}\n` : '') + body,  // 标题路径前缀保证自足
    });
  };

  let index = 0;
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const isHeading = /^#{1,3}\s/.test(line);
    const isBoundary = BOUNDARY.some(r => r.test(line));
    if (isHeading) headingPath = line.replace(/^#+\s*/, '');

    const lineT = tokensOf(line);
    if (isBoundary && cur.length || curTokens + lineT > maxTokens) {
      flush(index++);
      // 滑窗重叠：保留尾部 overlap 行
      cur = cur.slice(-overlap);
      curTokens = tokensOf(cur.join('\n'));
      curType = isHeading ? 'heading' : 'code';
    }
    cur.push(line); curTokens += lineT;
    if (curTokens > maxTokens * 1.5) { flush(index++); cur = []; curTokens = 0; } // 硬上限兜底
  }
  flush(index);
  return chunks;
}

// 测试
const md = `# 分页设计
介绍段...
## 实现
export function usePagination() {
  ${'逻辑行\n'.repeat(120)}  // 超长函数 → 滑窗
}`;
console.log(chunk(md, { maxTokens: 100 }).map(c => ({ t: c.type, tk: c.tokens, head: c.text.split('\n')[0].slice(0, 10) })));
```

**评分点**：
1. 结构边界优先（标题/函数声明/代码块围栏）而非纯长度切分——语义完整性是检索质量根基；
2. 超长单元的滑窗回退 + overlap 重叠（边界信息不丢失）；
3. 标题路径前缀注入每个 chunk——检索命中的片段脱离原文可读；
4. 硬上限兜底防单行超长（如压缩 JS）导致 chunk 爆炸；
5. 追问：函数体切分可结合 AST（按节点边界），正则版本是降级实现。
