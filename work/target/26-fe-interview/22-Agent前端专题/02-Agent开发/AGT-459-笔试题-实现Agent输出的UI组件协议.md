---
title: [AGT-459] 笔试题——实现 Agent 输出组件协议（白名单渲染+未知类型兜底）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-459：手写结构化输出渲染协议：块类型分发、props 校验、未知兜底、流式兼容

**需求与边界**：
- 输入：Agent 输出块数组 [{type, data, stream}]；输出：渲染计划。
- 边界要求：① 类型白名单分发（未注册类型不崩，降级文本展示）；② props 按注册 schema 校验（坏数据降级而非抛崩）；③ 流式块与整块区分（结构块数据齐才渲染）；④ XSS 防护（禁止任意 HTML，仅白名单组件）。

**答**：
```javascript
const REGISTRY = new Map([
  ['table', { comp: 'TableV', schema: TableProps }],
  ['chart', { comp: 'ChartV', schema: ChartProps }],
  ['code',  { comp: 'CodeV', schema: CodeProps }],
  ['text',  { comp: 'MdStream', schema: TextProps, streamable: true }],
]);
function planRender(blocks) {
  return blocks.map((b, i) => {
    const reg = REGISTRY.get(b.type);
    // 1. 未注册类型兜底：降级为文本（不崩）
    if (!reg) return { i, comp: 'FallbackText',
      props: { text: JSON.stringify(b.data).slice(0, 500) },
      fallback: true, reason: `未知类型 ${b.type}` };
    // 2. props 校验（坏数据降级）
    const check = reg.schema.safeParse(b.data);
    if (!check.success)
      return { i, comp: 'FallbackText',
        props: { text: `[${b.type} 数据异常]` },
        fallback: true, reason: check.error.message };
    // 3. 流式兼容：流式块（text）增量渲染；
    //    结构块（table/chart）数据齐才渲染
    if (!reg.streamable && b.stream && !b.complete)
      return { i, comp: 'Skeleton', until: 'complete' };
    return { i, comp: reg.comp, props: check.data };
  });
}
// 安全：组件白名单渲染（无 dangerouslySetInnerHTML），
// markdown 文本经 sanitize 后进 MdStream。
```

**评分点**:
- 白名单注册表分发 + 未知类型降级文本（永不白屏/崩溃）。
- props schema 校验，坏数据降级并带 reason（可调试）。
- 流式/整块双模式（结构块等 complete，骨架屏占位）。
- XSS 防护意识（无任意 HTML，markdown sanitize）。
