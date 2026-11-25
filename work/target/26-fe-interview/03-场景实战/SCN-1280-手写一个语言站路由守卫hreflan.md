---
title: [SCN-1280] 手写一个语言站路由守卫（hreflang 与重定向）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## SCN-1280：手写一个语言站路由守卫（hreflang 与重定向）

**答**：
- 需求：implement LangRouter(supported, defaultLang)。resolve(urlPath, saved, acceptLang) 判定最终语言：URL 前缀 > cookie 记忆 > Accept-Language > 默认；redirect(current, target) 生成重定向路径（保留查询参数）；hreflangTags(path) 生成 SEO 标签。
- 边界：URL 无前缀（/products）按检测语言重定向（可记住跳过）；unsupported lang 回默认；query 参数保留。
- 评分点：优先级链；重定向保留 query；hreflang；回退

```javascript
class LangRouter {
  constructor(supported, defaultLang = 'en') {
    this.supported = new Set(supported); this.def = defaultLang;
  }
  resolve(path, saved, acceptLang) {
    const seg = path.split('/')[1];
    if (this.supported.has(seg)) return seg;
    if (saved && this.supported.has(saved)) return saved;
    const al = acceptLanguage?.split(',')[0]?.split('-')[0];
    return this.supported.has(al) ? al : this.def;
  }
  redirect(path, target, { remember = true } = {}) {
    const u = new URL(path, 'https://x.example');
    u.pathname = `/${target}${u.pathname}`;
    return { url: u.pathname + u.search, remember,
      skipOnce: !remember };
  }
  hreflangTags(path) {
    return [...this.supported, 'x-default'].map(l =>
      `<link rel="alternate" hreflang="${l}" href="/${l}${path}">`);
  }
}
```
