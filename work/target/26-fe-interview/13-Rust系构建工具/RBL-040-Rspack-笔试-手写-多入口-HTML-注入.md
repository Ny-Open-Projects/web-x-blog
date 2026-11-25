---
title: [RBL-040] 笔试：手写简化版 HTML 注入插件（多入口 script 注入）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-040：笔试：手写简化版 HTML 注入插件（多入口 script 注入）
**答**：实现 HtmlMiniPlugin：1) 读取模板 HTML（含 </body>）；2) emit 阶段把所有入口 chunk 的 js 以 <script defer src> 注入 </body> 前、css 以 <link rel=stylesheet> 注入 </head> 前；3) 支持 options.template 与 options.publicPath；4) 输出 index.html 为新 asset；5) 已存在的同名 asset 要替换。

```javascript
class HtmlMiniPlugin {
  constructor(options = {}) {
    this.template = options.template || './index.html';
    this.publicPath = options.publicPath || '';
  }
  apply(compiler) {
    compiler.hooks.emit.tap('HtmlMiniPlugin', (compilation) => {
      const fs = require('fs');
      let html = fs.readFileSync(this.template, 'utf8');
      const { entryNames } = this.getEntries(compilation);
      const scripts = entryNames
        .map(n => Object.keys(compilation.assets).find(f => f.startsWith(n) && f.endsWith('.js')))
        .filter(Boolean)
        .map(f => `<script defer src="${this.publicPath}/${f}"></script>`)
        .join('\n');
      const links = Object.keys(compilation.assets)
        .filter(f => f.endsWith('.css'))
        .map(f => `<link rel="stylesheet" href="${this.publicPath}/${f}">`)
        .join('\n');
      html = html.replace('</head>', `${links}\n</head>`)
                 .replace('</body>', `${scripts}\n</body>`);
      compilation.emitAsset('index.html', {
        source: () => html, size: () => Buffer.byteLength(html),
      });
    });
  }
  getEntries(compilation) {
    const entry = compilation.options.entry;
    if (typeof entry === 'string' || Array.isArray(entry)) return { entryNames: ['main'] };
    return { entryNames: Object.keys(entry) };
  }
}
module.exports = HtmlMiniPlugin;
```
**评分点**：
- emit 钩子时机正确（assets 就绪，还能 emit/改）。
- js 注入 defer（不阻塞解析）——细节分。
- publicPath 拼接处理（CDN 场景）。
- 模板读取用同步 fs（emit 阶段 tap 同步）。
- 能指出真实 HtmlPlugin 还要做 favicon/注入去重/chunk 排序等边界。
