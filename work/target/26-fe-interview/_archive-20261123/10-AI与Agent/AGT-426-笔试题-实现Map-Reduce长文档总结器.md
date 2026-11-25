---
title: [AGT-426] 笔试题——实现长文档 Map-Reduce 总结（分段并行+归并+引用锚点）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-426：手写 500 页文档总结：按窗口分段、并行 map、reduce 归并、锚点回查

**需求与边界**：
- 输入：长文本、段窗口 token 数、map/reduce 函数；输出：总总结+各段摘要（可展开）。
- 边界要求：① 按语义边界分段（标题/段落）而非硬切；② 并行 map（Promise.all 限并发）；③ reduce 保留段引用（每条结论可定位到段号）；④ 数字原文保留（map 阶段不改写数字）。

**答**：
```javascript
async function mapReduceSummary(text, { windowTok = 3000, map, reduce,
  concurrency = 5 }) {
  // 1. 语义分段：标题优先，段落兜底
  const sections = splitByHeading(text, windowTok);
  // 2. 并行 map（限并发防限流）
  const summaries = [];
  let i = 0;
  async function worker() {
    while (i < sections.length) {
      const idx = i++;
      const s = sections[idx];
      summaries[idx] = { sec: idx, title: s.title,
        summary: await map(s.text, { keepNumbers: true }), // map 纪律
        anchor: s.start };                                 // 原文锚点
    }
  }
  await Promise.all(Array.from({ length: concurrency }, worker));
  // 3. reduce 归并（带段引用）
  const final = await reduce(summaries, {
    rule: `每个结论标注 [S{sec}] 段引用；
      数字必须与分段摘要一致，不得重算` });
  return { final, sections: summaries };
  // 前端：总总结折叠 + 分段摘要可展开（按需付费上下文）。
}
function splitByHeading(text, maxTok) {
  const blocks = text.split(/\n(?=#{1,3}\s)/);    // 标题切
  const out = []; let buf = '', start = 0, pos = 0;
  for (const b of blocks) {
    if (tok(buf) + tok(b) > maxTok && buf) {
      out.push({ text: buf, title: firstLine(buf), start });
      start = pos; buf = b;
    } else buf += (buf ? '\n' : '') + b;
    pos += b.length;
  }
  if (buf) out.push({ text: buf, title: firstLine(buf), start });
  return out;
}
```

**评分点**:
- 语义分段（标题优先+段落兜底）带起始偏移锚点，map 纪律（数字不改写）。
- 并行限并发（worker 池模式防限流），结果按索引回填保持顺序。
- reduce 强制段引用 [S{n}]，结论可定位回查——引用体系完整。
- 前端按需展开设计（总-分结构）的意识。
