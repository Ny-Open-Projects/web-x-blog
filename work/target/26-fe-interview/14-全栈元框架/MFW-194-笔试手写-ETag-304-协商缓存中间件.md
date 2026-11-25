---
title: [MFW-194] 笔试：手写 ETag / 304 协商缓存中间件
date: 2026-11-19
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-194：笔试：手写 ETag / 304 协商缓存中间件
**答**：为 SSR 应用实现 ETag 协商缓存中间件：① 渲染完成后计算响应体 ETag（内容 hash，弱 ETag `W/` 可选）；② 比对请求头 `If-None-Match`，命中则返回 304（无 body），跳过后续渲染发送；③ 支持 `*` 通配与多值匹配（逗号分隔列表）；④ 动态内容（登录态页面）不启用 ETag——按配置开关；⑤ 304 响应仍要带上 `Cache-Control`/`Vary` 头（304 不等于无缓存语义）。

```ts
import { createHash } from 'node:crypto';

function etagOf(body: string) {
  return `"${createHash('sha256').update(body).digest('base64url').slice(0, 27)}"`; // ① 强 ETag
}

function ifNoneMatchHit(header: string | null, etag: string) {
  if (!header) return false;
  const list = header.split(',').map((s) => s.trim()); // ③ 多值
  if (list.includes('*')) return true;                  // ③ 通配
  return list.some((t) => t === etag || t === `W/${etag}`); // 弱比较语义
}

export function etagMiddleware({ enabled = () => true } = {}) {
  return async (ctx: any, next: () => Promise<void>) => {
    await next(); // 先渲染拿到 body
    const body = ctx.body;
    if (typeof body !== 'string' || !enabled(ctx)) return; // ④ 动态页开关
    const etag = etagOf(body);
    ctx.set('ETag', etag);
    ctx.set('Cache-Control', 'no-cache'); // 必须重校验，缓存的 ETag 才有意义
    ctx.set('Vary', 'Cookie');            // ⑤ 个性化差异参与缓存键
    if (ifNoneMatchHit(ctx.get('If-None-Match'), etag)) {
      ctx.status = 304;
      ctx.body = null; // ② 无 body
    }
  };
}
```

**评分点**：
1. 顺序正确：先渲染后比对——ETag 需要最新内容才能判断 304，不能跳过渲染（这是与 CDN 层缓存最大的区别，能说清加分）。
2. `Cache-Control: no-cache` 搭配 ETag：每次都协商，而不是 no-store（协商缓存依赖浏览器保存上次响应元数据）。
3. If-None-Match 多值与 `*` 处理，304 时 body 为空但保留校验头。
4. 个性化页面按配置跳过 ETag（登录页每人都不同，ETag 会让命中率崩塌还白算 hash）。
5. 提到成本：大响应体 hash 本身有开销，实践上「静态资产走强 ETag/ Last-Modified，SSR HTML 多用 CDN 层缓存」。
