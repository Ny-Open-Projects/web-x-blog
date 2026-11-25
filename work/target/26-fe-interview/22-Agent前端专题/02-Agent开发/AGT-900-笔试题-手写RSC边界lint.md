---
title: [AGT-900] 手写 rscLint：server禁浏览器API、client禁数据获取、use client边界统计、误报豁免？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-900：手写 rscLint：server禁浏览器API、client禁数据获取、use client边界统计、误报豁免

**需求与边界**：
- 实现 rscLint(files)。
- 边界要求：① 无 'use client' 的文件中引用 window/document/localStorage/sessionStorage 即报；② 'use client' 文件中的直接 fetch 数据获取报（应下沉服务端）；③ 统计 use client 边界数量（>30% 提示边界下沉优化）；④ 豁免注释（// rsc-expect-error 行级豁免并计数）；⑤ 输出违规清单与边界统计。

**答**：
```javascript
const BROWSER_APIS = ['window', 'document', 'localStorage', 'sessionStorage'];
function rscLint(files) {
  const violations = []; let clientCount = 0;
  for (const f of files) {
    const isClient = /['"]use client['"]/.test(f.head);
    if (isClient) clientCount++;
    for (const line of f.lines) {
      if (line.includes('rsc-expect-error')) continue;  // 行级豁免
      if (!isClient && BROWSER_APIS.some(a =>
        new RegExp(`\b${a}\\.`).test(line)))
        violations.push({ file: f.path, line: line.no,
          kind: 'browser-api-in-server' });
      if (isClient && /\bfetch\(/.test(line)
        && !line.includes('swr') && !line.includes('query'))
        violations.push({ file: f.path, line: line.no,
          kind: 'data-fetch-in-client' });
    }
  }
  const ratio = clientCount / files.length;
  return { violations,
    clientRatio: ratio,
    hint: ratio > 0.3 ? 'use client 边界过多，考虑下沉服务端' : null };
}
```

**评分点**:
- 双向检查（server 禁浏览器 API/client 禁数据获取）——RSC 边界两大翻车点。
- 边界占比统计与优化提示（整树客户端化预警）。
- 行级豁免机制（误报可控）。

