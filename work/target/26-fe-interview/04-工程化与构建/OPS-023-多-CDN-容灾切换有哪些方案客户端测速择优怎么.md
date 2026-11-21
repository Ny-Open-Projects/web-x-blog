---
title: [OPS-023] 多 CDN 容灾切换有哪些方案？客户端测速择优怎么实现？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-023：多 CDN 容灾切换有哪些方案？客户端测速择优怎么实现？
**答**：
- DNS 层：权威 DNS/GSLB 对 CDN 域名做健康检查，故障自动切到备用 CDN 的 CNAME；生效受 TTL 影响（分钟级）。
- 网关层：自建一层轻代理（或云 WAF/网关）统一回源多 CDN，由网关路由，对前端透明。
- 客户端层：运行时对多个 CDN 域名测速（加载探针图片/脚本计时），选择最快者并持久化偏好；资源加载失败自动降级到下一家。
- 三层通常组合使用：DNS 做粗粒度切换，客户端做细粒度兜底；所有切换都要上报形成 CDN 质量报表。

```javascript
// cdn-picker.js：客户端测速择优 + 加载失败自动切换
const CANDIDATES = [
  'https://cdn.example.com',
  'https://cdn-b.example.com',
];

// 用一个 1x1 图片测 RTT：HEAD 请求不下载主体，计时取相对快慢
async function probe(host) {
  const t0 = performance.now();
  await fetch(`${host}/probe.png?t=${Date.now()}`,
    { mode: 'no-cors', cache: 'no-store' });
  return performance.now() - t0;
}

export async function pickCDN() {
  const cached = localStorage.getItem('cdn.pick');
  if (cached) return cached; // 上次选择在会话间保持，避免每次都测

  const results = await Promise.allSettled(CANDIDATES.map(probe));
  let best = CANDIDATES[0];
  let bestTime = Infinity;
  results.forEach((r, i) => {
    if (r.status === 'fulfilled' && r.value < bestTime) {
      best = CANDIDATES[i]; bestTime = r.value;
    }
  });
  localStorage.setItem('cdn.pick', best);
  navigator.sendBeacon('/report/cdn_pick', JSON.stringify(
    { pick: best, ms: Math.round(bestTime) }));
  return best;
}

// 资源加载：当前 CDN 失败自动顺序切换
export async function loadWithFailover(path) {
  for (const host of [await pickCDN(), ...CANDIDATES]) {
    try { return await fetch(`${host}/${path}`).then(r => r.json()); }
    catch (e) { continue; }
  }
  throw new Error('all CDN failed: ' + path);
}
```
