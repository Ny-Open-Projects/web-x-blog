---
title: [ARC-375] Edge/边缘计算与前端架构的边界如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-375：Edge/边缘计算与前端架构的边界如何设计？
**答**：
- 边缘运行的形态：CDN Workers（Cloudflare Workers/Vercel Edge）、边缘 KV、边缘 A/B 分桶、边缘 HTML 改写（ESI）。
- 适合下沉到边缘的：需要"离用户最近"的轻逻辑——入口 HTML 组装、灰度/AB 分桶（比端上分桶更可信）、鉴权校验与重定向、个性化注入（cookie 读取改写）、轻量 API 聚合。
- 不适合的：重业务状态、复杂事务、大内存计算（边缘实例限制 CPU 时间/内存）；数据库只在特定 region 时往返成本高。
- 前端架构视角：把边缘当作"第四层"（浏览器 → 边缘 → BFF → 服务），设计原则与 BFF 相同但更薄——只做路由、鉴权、改写，不做业务。
- 冷启动与一致性：边缘实例无长连接池（每次冷连），KV 最终一致（分桶名单同步延迟要评估，ARC-282）。
```javascript
// Cloudflare Worker：边缘 AB 分桶 + HTML 改写
export default {
  async fetch(req, env) {
    const bucket = await env.KV.get(`ab:${getUserId(req)}`) ?? hashBucket(getUserId(req));
    const res = await fetch(req);                    // 回源
    if (isHtml(res)) {
      const html = await res.text();
      return new Response(html.replace('__BUCKET__', bucket), res);  // 注入分桶
    }
    return res;
  }
}
```
