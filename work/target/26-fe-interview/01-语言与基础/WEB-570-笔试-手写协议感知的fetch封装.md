---
title: [WEB-570] 笔试：手写协议感知的 fetch 封装（自动降级）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 网络]
type: 笔试题
---

## WEB-570：笔试：手写协议感知的 fetch 封装（自动降级）

**答**：实现 `protoFetch(input, init)`：① 首次调用前探测 h3 可用性（复用探测结果缓存）；② h3 可用直接 fetch；③ h3 被拦（探测 blocked）时对同一域名改走配置的 h2 备用端点（如 `alt.h2.example.com`）或直接原样 fetch；④ 请求失败且是网络错误时降级重试一次（仅 GET）；⑤ 全部结果带 `x-proto` 字段返回实际协议。控制在 40 行内，注重边界。

```javascript
const probeCache = new Map();

async function detectH3(url) {
  const host = new URL(url).host;
  if (probeCache.has(host)) return probeCache.get(host);
  const r = await Promise.race([
    fetch(url, { method: 'HEAD', cache: 'no-store' })
      .then(res => {
        const [e] = performance.getEntriesByName(res.url);
        return e?.nextHopProtocol?.startsWith('h3') ? 'h3' : 'tcp';
      }),
    new Promise(res => setTimeout(() => res('blocked'), 2000)),
  ]).catch(() => 'blocked');
  probeCache.set(host, r);
  return r;
}

async function protoFetch(input, init = {}, alt = {}) {
  const url = typeof input === 'string' ? input : input.url;
  const proto = await detectH3(url);
  try {
    const res = await fetch(proto === 'blocked' && alt.h2Base
      ? url.replace(/^https:\/\/[^/]+/, alt.h2Base) : input, init);
    res.xProto = proto;
    return res;
  } catch (e) {
    if ((init.method || 'GET') !== 'GET') throw e; // 非幂等不自动重试
    const res = await fetch(input, init);
    res.xProto = proto;
    return res;
  }
}
```

**评分点**：
- 探测按 host 缓存且超时有上限，不会让每次业务请求都探测
- 协议不可用时按域名替换走备用端点，理解 Alt-Svc 缺失下的主动降级
- 自动重试限定 GET（幂等），写操作抛错由业务处理
- 结果携带实际协议字段，供监控上报闭环

## 变体与延伸（补充）

**变体与延伸**：

1. 探测为什么必须用 HEAD 且带 cache: 'no-store'？ → HEAD 无 body 开销小，no-store 防止命中已缓存的 h2 响应，否则 nextHopProtocol 反映的是旧连接导致误判。
2. 降级重试为什么严格限定 GET？ → 写请求重试可能重复提交产生副作用，幂等性无法保证，只能抛错交由业务层决定补偿策略。
3. 用 URL 替换到备用端点有什么隐患？ → 换域会触发跨域预检且 Cookie 不随行，备用域必须独立配置 CORS 与凭证，否则降级路径本身就会失败。
