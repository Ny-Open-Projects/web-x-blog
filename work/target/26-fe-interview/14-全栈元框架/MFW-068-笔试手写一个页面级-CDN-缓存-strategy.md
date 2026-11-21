---
title: [MFW-068] 笔试：手写一个页面级 CDN 缓存策略决策函数
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-068：笔试：手写一个页面级 CDN 缓存策略决策函数
**题目**：实现 `cacheHeaders(page)`，按页面类型返回 Cache-Control 头。规则：① 静态指纹资源 `public, max-age=31536000, immutable`；② 公开 SSR 页 `public, s-maxage=60, stale-while-revalidate=300`；③ 登录后页面 `private, no-store`；④ 含敏感查询参数的 URL 一律不缓存；⑤ API JSON 响应按传入 ttl 缓存但必须带 `Vary: Accept-Encoding`。

```ts
type PageType = 'static' | 'ssr-public' | 'authed' | 'api';

const SENSITIVE_KEYS = new Set(['token', 'session', 'code', 'access_token']);

function hasSensitiveQuery(url: URL): boolean {
  return [...url.searchParams.keys()].some((k) => SENSITIVE_KEYS.has(k.toLowerCase()));
}

export function cacheHeaders(
  type: PageType,
  opts: { url: string; ttl?: number } = { url: '' },
): Record<string, string> {
  const url = new URL(opts.url, 'https://example.com');

  // 规则④：敏感参数优先级最高，任何类型都不缓存
  if (hasSensitiveQuery(url)) {
    return { 'Cache-Control': 'no-store, private', 'Vary': 'Accept-Encoding' };
  }

  switch (type) {
    case 'static': // 指纹资源：路径带 hash，可放心一年
      return { 'Cache-Control': 'public, max-age=31536000, immutable' };
    case 'ssr-public': // CDN 挡洪峰 + SWR 宽限
      return { 'Cache-Control': 'public, s-maxage=60, stale-while-revalidate=300' };
    case 'authed': // 个性化内容绝不共享缓存
      return { 'Cache-Control': 'private, no-store' };
    case 'api': {
      const ttl = Math.max(0, opts.ttl ?? 0);
      // ttl=0 时退化为 no-cache（允许缓存但必须校验），而非 no-store 误伤
      const cc = ttl === 0
        ? 'public, no-cache'
        : `public, s-maxage=${ttl}, stale-while-revalidate=${Math.floor(ttl * 2)}`;
      return { 'Cache-Control': cc, 'Vary': 'Accept-Encoding' };
    }
  }
}
```

**评分点**：
1. 敏感参数拦截放在 switch 之前，体现「安全优先于性能」的判断顺序。
2. authed 页面用 `private, no-store`，知道 `private` 是防止 CDN/代理共享的关键字。
3. static 用 immutable，能说出它避免浏览器条件请求 304 的意义。
4. API 分支对 ttl=0 有退化处理而不是机械拼接 `s-maxage=0`。
5. Vary 头正确设置（仅 Accept-Encoding），能说出 Vary: Cookie 会击穿缓存。
