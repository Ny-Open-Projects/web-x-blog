---
title: [MFW-744] 笔试：手写 routeRules 头推导器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-744：笔试：手写 routeRules 推导器

**答**：实现 `resolveRouteRules(path, rules)`。rules: `Record<pattern, Rule>`；Rule: `{ swr?: number, isr?: number, cache?: boolean|object, headers?: Record, redirect?: { to, statusCode? }, prerender?: boolean }`。规则：1) **匹配**：specific > 通配（`/blog/featured` 优先于 `/blog/**`）；2) swr/isr → Cache-Control 头（RBL-743）；prerender → 构建期标记（无响应头——构建产物）；3) headers 直接合并；redirect → 302/301 头；cache: false → no-store；4) 多规则叠加（headers 与 cache 共存）；5) 返回 `{ headers: Record, redirect?, prerender? }`。边界：无匹配规则（默认 {}）；空 path；`**` 匹配所有。

```javascript
function matchPattern(pattern, path) {
  if (pattern === path) return { match: true, specific: true };
  if (pattern.endsWith('/**'))
    return { match: path.startsWith(pattern.slice(0, -4)), specific: false };
  if (pattern.endsWith('/*'))
    return { match: path.startsWith(pattern.slice(0, -2)) && !path.slice(pattern.length - 2).includes('/'), specific: false };
  return { match: false, specific: false };
}
function resolveRouteRules(path, rules = {}) {
  // 按 specificity 排序：精确 > 通配
  const sorted = Object.entries(rules).sort((a, b) => {
    const sa = matchPattern(a[0], path).specific ? 0 : 1;
    const sb = matchPattern(b[0], path).specific ? 0 : 1;
    if (sa !== sb) return sa - sb;
    return b[0].length - a[0].length;                    // 更长 pattern 更 specific
  });
  let headers = {}; let redirect, prerender;
  for (const [pattern, rule] of sorted) {
    const m = matchPattern(pattern, path);
    if (!m.match) continue;
    if (rule.swr != null)
      headers['cache-control'] = `s-maxage=${rule.swr}, stale-while-revalidate`;
    else if (rule.isr != null)
      headers['cache-control'] = `s-maxage=${rule.isr}`;
    else if (rule.cache === false)
      headers['cache-control'] = 'no-store';
    if (rule.redirect) { redirect = rule.redirect; break; }
    if (rule.prerender) prerender = true;
    if (rule.headers) headers = { ...headers, ...rule.headers };
    break;                                               // 首个匹配即用
  }
  return { headers, redirect, prerender };
}

// 自测
const rules = {
  '/': { prerender: true },
  '/blog/**': { swr: 3600 },
  '/blog/featured': { swr: 0 },
  '/api/**': { cache: false, headers: { 'x-cors': '1' } },
  '/old': { redirect: { to: '/new', statusCode: 302 } },
};
// 精确匹配优先
let r = resolveRouteRules('/blog/featured', rules);
console.log(r.headers['cache-control'].includes('s-maxage=0'));   // featured 用 0（实时）
// 通配
r = resolveRouteRules('/blog/post-1', rules);
console.log(r.headers['cache-control'].includes('s-maxage=3600'));
// API 组合
r = resolveRouteRules('/api/products', rules);
console.log(r.headers['cache-control'] === 'no-store');
console.log(r.headers['x-cors'] === '1');                // headers 合并
// 重定向
r = resolveRouteRules('/old', rules);
console.log(r.redirect.to === '/new' && r.redirect.statusCode === 302);
// prerender
r = resolveRouteRules('/', rules);
console.log(r.prerender === true);
// 无匹配
r = resolveRouteRules('/nomatch', rules);
console.log(Object.keys(r.headers).length === 0);
```

**评分点**：
- 匹配优先级（specific > 通配——`/blog/featured` 优先于 `/blog/**`）；首匹配即停
- 多规则叠加（cache-control + headers 合并——swr 与自定义头共存）
- 边界（无匹配/空 path/redirect 打断）；swr/isr/prerender/cache:false 的语义翻译
- 能说清「routeRules 的声明式缓存 = 配置中心化 + specific 优先——RBL-582 的 Nuxt 版本」属于加分
