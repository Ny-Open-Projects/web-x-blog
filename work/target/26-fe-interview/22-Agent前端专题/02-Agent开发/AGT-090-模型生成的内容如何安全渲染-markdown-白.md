---
title: [AGT-090] 模型生成的内容如何安全渲染（markdown 白名单 + 链接校验）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-090：模型生成的内容如何安全渲染（markdown 白名单 + 链接校验）？
**答**：
- 模型输出是不可信输入：可能包含 XSS 载荷、`javascript:` 链接、钓鱼外链，渲染前必须白名单净化。
- 净化策略：标签 allowlist（只放行 p/strong/code/a/table 等有限集合）、属性 allowlist、非白名单标签整体移除。
- 链接校验：协议只允许 http(s)，封杀 `javascript:`/`data:`；外链加 `rel="noopener noreferrer"` 并提示目标域，防钓鱼。
- React 默认转义，但 `dangerouslySetInnerHTML` 是逃生门——markdown 渲染路径必须先过净化再注入。

```typescript
import { z } from 'zod';

// 白名单净化：标签 allowlist + 协议校验
const ALLOWED_TAGS = new Set(['p', 'br', 'strong', 'em', 'code', 'pre', 'ul', 'ol', 'li', 'blockquote', 'h1', 'h2', 'h3', 'a', 'table', 'thead', 'tbody', 'tr', 'th', 'td']);
const ALLOWED_ATTRS = new Set(['href', 'title', 'class']);

export function sanitizeGeneratedHtml(html: string): string {
  const doc = new DOMParser().parseFromString(html, 'text/html');
  const walk = (node: Element) => {
    for (const child of [...node.children]) {
      if (!ALLOWED_TAGS.has(child.tagName.toLowerCase())) { child.remove(); continue; } // 非白名单整体移除
      for (const attr of [...child.attributes]) {
        if (!ALLOWED_ATTRS.has(attr.name.toLowerCase())) child.removeAttribute(attr.name);
      }
      const href = child.getAttribute('href');
      if (href) {
        const u = new URL(href, location.origin);
        if (u.protocol !== 'http:' && u.protocol !== 'https:') { child.remove(); continue; } // 封杀 javascript 与 data 协议
        if (u.origin !== location.origin) child.setAttribute('rel', 'noopener noreferrer'); // 外链防钓鱼
      }
      walk(child);
    }
  };
  walk(doc.body);
  return doc.body.innerHTML;
}

// React 渲染出口：markdown → html → 净化 → 注入
function SafeMarkdown({ md }: { md: string }) {
  return <div dangerouslySetInnerHTML={{ __html: sanitizeGeneratedHtml(renderMarkdown(md)) }} />;
}
```

---

## 十九、评测与质量工程
