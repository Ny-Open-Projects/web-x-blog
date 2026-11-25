---
title: [MFW-197] 笔试：手写 Astro island 标记解析器
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-197：笔试：手写 Astro island 标记解析器
**答**：Astro 渲染后 HTML 里的 island 形如 `<astro-island uid="z1Ab" component-url="/Counter.js" component-export="default" renderer-url="/client.js" props='{"count":3}' client="visible" ssr="...">...</astro-island>`。实现解析器 `parseIslands(html)`：① 提取页面所有 island 的元信息（uid、组件、client 指令、props）；② props 是 JSON 属性，注意单引号包裹与嵌套引号（不能粗暴 split）；③ 统计报告：按 client 指令分类数量、预计需要下载的 JS 模块去重集合；④ 处理嵌套 island（内层不算独立触发点，只统计外层）；⑤ 非法 island（缺 component-url）收集进 errors 而不是抛异常中断。

```ts
const ATTRS = /<astro-island\b([^>]*)>/g;
const GET = (attrs: string, name: string) => {
  // ② 匹配单/双引号属性，内部引号不提前截断
  const re = new RegExp(`${name}\\s*=\\s*(?:"((?:[^"]|\\\\")*)"|'((?:[^']|\\\\')*)')`);
  const m = attrs.match(re);
  return (m?.[1] ?? m?.[2] ?? '').replace(/\\(['"])/g, '$1');
};

export function parseIslands(html: string) {
  const islands: any[] = []; const errors: string[] = [];
  let depth = 0, m: RegExpExecArray | null;
  ATTRS.lastIndex = 0;
  while ((m = ATTRS.exec(html))) {
    const isSelfClosing = m[0].endsWith('/>');
    const url = GET(m[1], 'component-url');
    if (!url) { errors.push(`island@${m.index} missing component-url`); continue; } // ⑤
    if (!isSelfClosing) depth++; // ④ 简化：astro-island 标签配对计数
    const client = GET(m[1], 'client') || 'load';
    const props = safeJson(GET(m[1], 'props'));
    islands.push({
      uid: GET(m[1], 'uid'),
      component: url.split('/').pop()!.replace(/\.js$/, ''),
      client, props,
      nested: depth > 1, // 内层 island 标记为嵌套
    });
  }
  const modules = new Set(islands.filter(i => !i.nested).map(i => i.component)); // ③/④
  return {
    islands, errors,
    report: {
      byClient: islands.reduce((a, i) => ((a[i.client] = (a[i.client] ?? 0) + 1), a), {}),
      modules: [...modules], // 去重后需要下载的模块
    },
  };
}

function safeJson(s: string) { try { return JSON.parse(s); } catch { return null; } }
```

**评分点**：
1. 属性提取用引号感知的正则/解析，不做裸 split（props 里常见嵌套引号，裸切必错）。
2. props JSON 解析失败返回 null 并继续，单个 island 坏不拖垮整页分析。
3. 嵌套 island 只统计外层为独立触发点（激活成本以顶层岛为单位），有这个意识。
4. 报告输出「需下载模块去重集合」——这正是 islands 架构省 JS 的核心度量。
5. errors 收集不抛异常，体现解析器面向构建期检查工具的健壮性要求。
