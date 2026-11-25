---
title: [SCN-1295] 手写一个多语言站 SEO 结构生成器
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## SCN-1295：手写一个多语言站 SEO 结构生成器

**答**：
- 需求：implement SeoStructure(base, langs)。urls(path) 生成各语言 URL；sitemap() 生成 sitemap 条目（含 hreflang 交替链接）；canonical(path, lang) 生成 canonical 标签（防重复内容）。
- 边界：langs 至少 1 个；path 去尾部斜杠；x-default 指向默认语言；base URL 去尾斜杠。
- 评分点：URL 结构；canonical；x-default；斜杠处理

```javascript
class SeoStructure {
  constructor(base, langs, defaultLang = 'en') {
    this.base = base.replace(/\/$/, '');
    this.langs = langs; this.def = defaultLang;
  }
  urls(path) {
    const p = path.replace(/\/$/, '');
    return this.langs.map(l => ({ lang: l, url: `${this.base}/${l}${p}` }));
  }
  canonical(path, lang) {
    return `<link rel="canonical" href="${this.base}/${lang}${path}">`;
  }
  sitemap(path) {
    return { entries: this.urls(path),
      alternates: this.langs.map(l => ({ hreflang: l,
        url: `${this.base}/${l}${path}` }))
        .concat([{ hreflang: 'x-default', url: `${this.base}/${this.def}${path}` }]) };
  }
}
```
