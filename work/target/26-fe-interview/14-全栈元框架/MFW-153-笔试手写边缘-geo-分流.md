---
title: [MFW-153] 笔试：手写一个边缘 geo 分流中间件
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-153：笔试：手写一个边缘 geo 分流中间件
**答**：在边缘（类 Cloudflare Workers/Next Middleware 环境）实现 geo 分流：① 按请求头 `x-vercel-ip-country`/`cf-ipcountry` 识别国家；② 中国大陆访问 `/products/**` 时 302 到 `cn.example.com` 同路径；③ 其余地区注入 `x-served-region` 头继续；④ 支持强制测试参数 `?geo=US` 覆盖（仅调试模式）；⑤ 分流决策要可缓存（避免每请求计算）。

```ts
type GeoEnv = { DEBUG: boolean };

const CN_REDIRECT_HOST = 'https://cn.example.com';
const MAINLAND = new Set(['CN']);
const cacheableDecision = new Map<string, { to: string | null; until: number }>();
const TTL = 60_000;

function detectCountry(req: Request, url: URL, env: GeoEnv): string {
  // 调试覆盖：仅 DEBUG 环境生效，防止生产被伪造头绕过
  if (env.DEBUG) {
    const force = url.searchParams.get('geo');
    if (force) return force.toUpperCase();
  }
  const header = req.headers.get('x-vercel-ip-country') ?? req.headers.get('cf-ipcountry');
  return (header ?? 'XX').toUpperCase();
}

export async function geoSplit(req: Request, env: GeoEnv): Promise<Response> {
  const url = new URL(req.url);

  // 决策缓存：同一 (country, path-prefix) 一分钟内复用，减少边缘 CPU
  const cacheKey = `${detectCountry(req, url, env)}|${url.pathname.startsWith('/products')}`;
  const cached = cacheableDecision.get(cacheKey);
  if (cached && cached.until > Date.now()) {
    if (cached.to) return Response.redirect(cached.to + url.search, 302);
    return passthrough(req);
  }

  const country = detectCountry(req, url, env);
  let decision: { to: string | null; until: number };

  if (MAINLAND.has(country) && url.pathname.startsWith('/products')) {
    decision = { to: CN_REDIRECT_HOST + url.pathname, until: Date.now() + TTL };
    cacheableDecision.set(cacheKey, decision);
    return Response.redirect(decision.to + url.search, 302); // 302 保持可回切
  }

  decision = { to: null, until: Date.now() + TTL };
  cacheableDecision.set(cacheKey, decision);
  const res = passthrough(req);
  res.headers.set('x-served-region', country); // 下游感知区域
  return res;
}

function passthrough(req: Request): Response {
  return new Response(null, { status: 200, headers: new Headers() });
}
```

**评分点**：
1. 双头兼容读取（Vercel/Cloudflare 头名不同），缺失时兜底 'XX'。
2. 调试覆盖仅在 DEBUG 开启——生产可被伪造头绕过是常见漏洞。
3. 302 而非 301（分流策略要可回切，永久重定向会固化在浏览器）。
4. query 串保留在重定向目标上。
5. 决策缓存意识（或说清 Edge Cache API / KV 方案）与每请求 CPU 成本。
