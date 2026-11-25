---
title: [MFW-709] 笔试：手写 locale 路由生成器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-709：笔试：手写 locale 路由生成器

**答**：实现 `generateLocaleParams(locales, pages)` 与 `validateLocaleRoutes(routes, supportedLocales)`。generateLocaleParams：pages × locales 的笛卡尔积（每页每 locale 一个 params 对象）。validateLocaleRoutes：1) 路由的 locale 段必须是受支持的 locale（/xx/unsupported → finding 'unsupported-locale'）；2) 路由缺 locale 段（无 locale 的直接路径——需 middleware 兜底重定向）→ info 'bare-path'（middleware 重定向覆盖）；3) 重复路由（同 locale 同路径两个定义）→ error 'duplicate'。返回 `{ params, findings }`。边界：locales 空（无 params——纯单语言）；pages 空；unsupported locale 有 fallback 语言。

```javascript
function generateLocaleParams(locales = [], pages = []) {
  return pages.flatMap(page =>
    locales.map(locale => ({ locale, ...page.params })));
}
function validateLocaleRoutes(routes = [], supportedLocales = []) {
  const findings = [];
  const seen = new Set();
  for (const route of routes) {
    const segments = route.split('/').filter(Boolean);
    const locale = segments[0];
    const isLocaleSegment = locale && !route.startsWith('/api/');
    if (isLocaleSegment && !supportedLocales.includes(locale))
      findings.push({ route, type: 'unsupported-locale', locale });
    if (!isLocaleSegment && segments.length > 0 && !route.startsWith('/api'))
      findings.push({ route, type: 'bare-path', detail: '需 middleware 重定向到 locale 路径' });
    if (seen.has(route)) findings.push({ route, type: 'duplicate' });
    seen.add(route);
  }
  return { findings };
}

// 自测
const locales = ['en', 'zh', 'ja'];
const pages = [{ params: { slug: 'intro' } }, { params: { slug: 'guide' } }];
let params = generateLocaleParams(locales, pages);
console.log(params.length === 6);                        // 3 locale × 2 page
console.log(params[0].locale === 'en' && params[0].slug === 'intro');
console.log(params[3].locale === 'zh');

// 路由校验
const routes = [
  '/en/products', '/zh/products',                        // 合法
  '/xx/products',                                         // unsupported
  '/products',                                            // bare（middleware 兜底）
  '/api/health',                                          // API 跳过
  '/en/products',                                         // duplicate
];
let r = validateLocaleRoutes(routes, locales);
console.log(r.findings.some(f => f.type === 'unsupported-locale' && f.locale === 'xx'));
console.log(r.findings.some(f => f.type === 'bare-path' && f.route === '/products'));
console.log(r.findings.some(f => f.type === 'duplicate'));
console.log(r.findings.filter(f => f.type === 'bare-path').length === 1);   // api 不算 bare
// API 路由不算 unsupported
console.log(!r.findings.some(f => f.route === '/api/health'));

// 空
console.log(generateLocaleParams([], pages).length === 0);
console.log(generateLocaleParams(locales, []).length === 0);
```

**评分点**：
- 笛卡尔积正确（pages × locales——generateStaticParams 的 locale 版 RBL-708）；locale 段校验
- 三类 finding（unsupported/bare/duplicate）；API 路由豁免（/api 不走 locale 段）
- 边界（空 locales/pages）；bare-path 的 middleware 兜底语义
- 能说清「locale 段路由的缓存一致性优于 cookie locale——locale 进 URL = 进缓存键零串语言」属于加分
