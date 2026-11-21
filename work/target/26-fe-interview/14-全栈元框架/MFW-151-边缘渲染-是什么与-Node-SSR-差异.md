---
title: [MFW-151] 边缘渲染是什么？和传统 Node SSR 的差异与取舍？
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-151：边缘渲染是什么？和传统 Node SSR 的差异与取舍？
**答**：
- 边缘渲染：SSR 代码跑在 CDN 节点的轻量 isolate（Cloudflare Workers/Vercel Edge）里，用户就近取到渲染结果——TTFB 从「区域机房往返」降到「同城边缘往返」。
- 差异对比：Node SSR = 完整运行时（任意 npm 包、长连接池）但集中在少数机房；Edge = 冷启动近零、全球分布，但**运行时阉割**（无 TCP、有限 CPU 时间、内存上限）。
- 架构对策：重数据访问下沉到「区域中心服务」（HTTP RPC），边缘只做路由改写/轻渲染/鉴权——「边缘薄、中心厚」的分层。
- 成本与一致性：Edge 计费按请求/CPU 更细，但边缘节点访问源站 DB 的往返要计入延迟；KV/DO 类边缘存储成为新依赖。
- 选型直觉：全球受众、轻个性化页面 → Edge 收益大；国内单区域 + 重 DB 渲染 → Node 容器够用。

```ts
// Edge 渲染的分层姿势（Cloudflare Workers 为例）

// edge/middleware.ts —— 边缘层：轻判断 + 数据从中心 API 取
export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const url = new URL(req.url);
    const country = req.cf?.country ?? 'CN';

    // 个性化判断留在边缘（毫秒级）
    if (url.pathname === '/checkout') {
      const region = ['CN', 'JP'].includes(country) ? 'ap' : 'us';
      // 重数据：调用区域中心服务（HTTP，非 TCP）
      const data = await fetch(`https://${region}-api.example.com/cart`, {
        headers: { cookie: req.headers.get('cookie') ?? '' },
      });
      return new HTMLRewriter()
        .on('#cart-total', { element(e) { e.setInnerContent(data.ok ? '已同步' : '同步失败'); } })
        .transform(new Response(await renderShell(), htmlHeaders));
    }
    return renderStatic(url); // 静态资源直接边缘命中
  },
};
```
