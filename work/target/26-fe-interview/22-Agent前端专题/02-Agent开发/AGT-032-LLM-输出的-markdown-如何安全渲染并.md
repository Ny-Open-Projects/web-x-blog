---
title: [AGT-032] LLM 输出的 markdown 如何安全渲染并做代码高亮？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-032：LLM 输出的 markdown 如何安全渲染并做代码高亮？
**答**：
- 管线：marked/markdown-it 解析 → highlight.js/Shiki 高亮 → DOMPurify 消毒 → `v-html`/`dangerouslySetInnerHTML`。
- LLM 输出不可信，prompt 注入可以让它输出 `<img onerror>` 等恶意 HTML，消毒是不可省略的一步。
- 自定义 renderer 处理代码块：按语言高亮，未识别语言降级 plaintext。
- 流式期间 markdown 处于"未闭合"状态（代码块没写完），可用增量渲染或对不完整块降级为纯文本。

```typescript
// markdown 管线：marked 解析 + highlight.js 高亮 + DOMPurify 消毒
import { marked } from 'marked';
import hljs from 'highlight.js';
import DOMPurify from 'dompurify';

const renderer = new marked.Renderer();

renderer.code = ({ text, lang }: { text: string; lang?: string }) => {
  const language = lang && hljs.getLanguage(lang) ? lang : 'plaintext';
  const html = hljs.highlight(text, { language }).value;
  return `<pre><code class="hljs language-${language}">${html}</code></pre>`;
};

marked.use({ renderer, breaks: true, gfm: true });

export function renderMarkdown(md: string): string {
  const rawHtml = marked.parse(md, { async: false }) as string;
  return DOMPurify.sanitize(rawHtml, {
    FORBID_TAGS: ['style', 'iframe', 'form'],
    FORBID_ATTR: ['onerror', 'onclick', 'onload'], // 防 prompt 注入外带脚本
  });
}
```
