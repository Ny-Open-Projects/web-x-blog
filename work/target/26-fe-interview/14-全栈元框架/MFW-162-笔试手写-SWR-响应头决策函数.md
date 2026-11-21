---
title: [MFW-162] 笔试：手写一个 SWR 响应头决策函数
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-162：笔试：手写一个 SWR 响应头决策函数
**题目**：实现 `swrHeaders(input)`：① 输入含内容类型、敏感度、TTL 偏好；② 输出合规 Cache-Control：敏感内容一律 `private, no-store`；公开内容 `public, s-maxage=N, stale-while-revalidate=M`，且 M ≥ 2N；③ 请求带 `Authorization` 头时降级为 private 缓存（浏览器可用、CDN 不共享）；④ TTL=0 时输出 `no-cache`（可缓存但需校验）而非 no-store；⑤ 产出同时含 `Age`/`X-SWR-Source` 观测头（缓存命中来源）。

```ts
type Input = {
  sensitive: boolean;
  ttl?: number;             // 期望 CDN 缓存秒数
  hasAuthHeader?: boolean;  // 请求带 Authorization
  source?: 'cdn-hit' | 'stale-hit' | 'origin';
};

function swrHeaders(input: Input): Record<string, string> {
  const headers: Record<string, string> = {};

  // ③ 带鉴权头：CDN 不共享，浏览器可私缓存
  if (input.sensitive || input.hasAuthHeader) {
    headers['Cache-Control'] = input.sensitive
      ? 'private, no-store'          // ② 敏感：彻底不存
      : 'private, max-age=60';       // 降级为浏览器私有缓存
    return headers;
  }

  const ttl = input.ttl ?? 0;
  // ④ TTL=0：no-cache（可存但每次校验），不是 no-store（彻底不存）
  if (ttl === 0) {
    headers['Cache-Control'] = 'public, no-cache';
  } else {
    headers['Cache-Control'] =
      `public, s-maxage=${ttl}, stale-while-revalidate=${ttl * 2}`; // M = 2N
  }

  // ⑤ 观测头：命中来源可追踪命中率
  if (input.source) {
    headers['X-SWR-Source'] = input.source;
    headers['Age'] = input.source === 'origin' ? '0' : String(Math.floor(ttl / 2));
  }
  headers.Vary = 'Accept-Encoding';
  return headers;
}

// —— 用例 ——
console.log(swrHeaders({ sensitive: true }).['Cache-Control']); // private, no-store
console.log(swrHeaders({ sensitive: false, hasAuthHeader: true }).['Cache-Control']); // private, max-age=60
console.log(swrHeaders({ sensitive: false, ttl: 60 }).['Cache-Control']);
// public, s-maxage=60, stale-while-revalidate=120
console.log(swrHeaders({ sensitive: false, ttl: 0 }).['Cache-Control']); // public, no-cache
```

**评分点**：
1. 敏感与带 Authorization 的区分：敏感=不存，鉴权=私有缓存——两种语义不混。
2. no-cache 与 no-store 区分清晰（可缓存需校验 vs 不缓存）。
3. SWR 窗口大于 s-maxage（2N），能说出窗口小于 N 会退化成同步回源。
4. Vary 最小化，绝不出现 Vary: Cookie。
5. 观测头意识：X-SWR-Source/Age 便于命中率排查。
