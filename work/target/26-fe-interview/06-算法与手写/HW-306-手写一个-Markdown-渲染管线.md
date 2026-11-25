---
title: [HW-306] 手写一个 Markdown 渲染管线：块级解析与行内解析两阶段
date: 2026-11-21
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

## HW-306：手写一个 Markdown 渲染管线：块级解析与行内解析两阶段

**答**：
- 需求：实现 MiniMD：块级解析（标题/列表/代码块/引用/段落切分）→ 每块行内解析（**粗体**、*斜体*、`代码`、[链接](url)）→ 拼 HTML；输出安全（链接 href 白名单 http/https，防 javascript:）。
- 边界：代码块内容不进行行内解析（原样转义）；嵌套列表缩进；链接白名单；行内规则按优先级（代码优先于粗体防 `` 冲突）。
- 评分点：两阶段分离；代码块跳过行内解析；href 白名单。

```javascript
const FENCE = '\u0060'.repeat(3);   // 三反引号围栏（码点构造，避免源码内出现字面围栏）
function miniMD(md) {
  const lines = md.split('\n');
  const blocks = [];
  let i = 0;
  while (i < lines.length) {
    const l = lines[i];
    if (l.startsWith(FENCE)) {                               // 代码块：不解析行内
      const buf = []; i++;
      while (i < lines.length && !lines[i].startsWith(FENCE)) buf.push(lines[i++]);
      i++;
      blocks.push(`<pre><code>${esc(buf.join('\n'))}</code></pre>`);
      continue;
    }
    const h = l.match(/^(#{1,6})\s+(.*)/);
    if (h) { blocks.push(`<h${h[1].length}>${inline(h[2])}</h${h[1].length}>`); i++; continue; }
    if (/^[-*]\s/.test(l)) {                                  // 列表块
      const items = [];
      while (i < lines.length && /^[-*]\s/.test(lines[i])) items.push(`<li>${inline(lines[i++].slice(2))}</li>`);
      blocks.push(`<ul>${items.join('')}</ul>`);
      continue;
    }
    if (l.startsWith('> ')) { blocks.push(`<blockquote>${inline(l.slice(2))}</blockquote>`); i++; continue; }
    if (l.trim() === '') { i++; continue; }
    blocks.push(`<p>${inline(l)}</p>`); i++;
  }
  return blocks.join('\n');
}
function inline(s) {                                        // 行内：代码优先
  s = esc(s);
  s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  s = s.replace(/\*([^*]+)\*/g, '<em>$1</em>');
  s = s.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, t, href) =>
    /^(https?:|\/)/.test(href) ? `<a href="${href}">${t}</a>` : t);   // href 白名单
  return s;
}
const esc = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
```
