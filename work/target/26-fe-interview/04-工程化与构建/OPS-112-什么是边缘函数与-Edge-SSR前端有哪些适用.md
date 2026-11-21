---
title: [OPS-112] 什么是边缘函数与 Edge SSR？前端有哪些适用场景与边界？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-112：什么是边缘函数与 Edge SSR？前端有哪些适用场景与边界？
**答**：
- 边缘函数：JS 运行时部署在 CDN 边缘节点（Cloudflare Workers、Vercel Edge、阿里云 ERB），毫秒级冷启动、离用户一跳。
- 典型场景：A/B 与灰度分流（OPS-107 的边缘版）、请求头注入/改写、轻量 HTML 改写、鉴权前置、地理就近路由。
- Edge SSR：在边缘渲染 HTML，比中心机房 SSR 省去跨地域回源延迟；适合营销页、入口壳，不适合重计算与长连接。
- 边界：CPU 时间与内存受限、无法持久连接数据库（一般配合区域化 D1/DO 类存储）、调试与可观测性链路要单独建设。
- 成本模型按请求数 + CPU 时长计费，高频轻逻辑收益大，重业务逻辑仍放中心/容器。

```javascript
// 边缘函数示例：边缘侧灰度分流 + 入口改写，源站不感知灰度逻辑
export default {
  async fetch(request) {
    const url = new URL(request.url);

    // 灰度桶：cookie 命中 beta 的用户，以及 5% 随机流量，走 v2 目录
    const bucket = request.headers.get('cookie')?.includes('beta=1')
      ? 'v2'
      : (Math.random() < 0.05 ? 'v2' : 'v1');

    if (url.pathname === '/') {
      // 边缘回源对应版本入口，并在响应头标记分桶（看板归因用）
      const resp = await fetch(`https://origin.example.com/${bucket}/index.html`);
      const html = await resp.text();
      return new Response(html, {
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'x-edge-bucket': bucket,
          'cache-control': 'no-cache',
        },
      });
    }

    // 其余请求直接透传（静态资源由 CDN 正常命中）
    return fetch(request);
  },
};
```
