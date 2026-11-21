---
title: [OPT-149] 发布新版本后，如何自动"预热"CDN/缓存避免首发用户变慢？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-149：发布新版本后，如何自动"预热"CDN/缓存避免首发用户变慢？

**答**：
- 问题：发版后 hash 变了，CDN 边缘节点全是 MISS，第一波用户全打到源站，慢且容易把源站打挂。
- 预热三件事：①静态产物 CDN 预热（各云厂商都有预热 API/接口，发布流水线里对 Top URL 清单触发）；②HTML/接口缓存预热（发布后立刻用真实 UA 访问一遍关键页面，让 SSR 缓存/接口缓存提前填充）；③Service Worker 预缓存清单同步更新。
- URL 清单来源：实时访问日志 Top N 路由 + 运营指定的大促页面，脚本化维护。
- 验证：预热后抽样 curl 检查 `x-cache: HIT` 覆盖率，低于阈值告警。

```javascript
// 一一对应：发布后自动预热脚本（CDN 预热 API + 缓存穿透访问 + HIT 校验）
// scripts/warmup.mjs —— 接在 CI 部署 job 之后运行
const TOP_URLS_FILE = 'warmup-urls.txt';   // 从访问日志离线生成的 Top 300 路由
const base = process.env.DEPLOY_DOMAIN;    // https://www.example.com

async function cdnPrefetch(paths) {
  // 各云厂商 CDN 预热接口大同小异：POST URL 列表，边缘节点后台回源
  await fetch('https://cdn-api.example.com/v2/prefetch', {
    method: 'POST',
    headers: { Authorization: `Bearer ${process.env.CDN_TOKEN}` },
    body: JSON.stringify({ urls: paths.map(p => base + p) }),
  });
}

async function warmAppCaches(paths) {
  // 用真实 UA 访问一遍：填充 SSR 片段缓存、接口缓存、SW 预缓存源
  const ua = 'Mozilla/5.0 (Macintosh) Chrome/120 Safari/537.36';
  for (const p of paths) {
    await Promise.allSettled([
      fetch(base + p, { headers: { 'user-agent': ua } }),          // HTML/SSR
      fetch(`${base}/api/home?path=${encodeURIComponent(p)}`, { headers: { 'user-agent': ua } }), // 接口
    ]);
  }
}

async function verifyHitRatio(paths) {
  let hit = 0;
  for (const p of paths) {
    const res = await fetch(base + p);
    if (/HIT/.test(res.headers.get('x-cache') || '')) hit++;
  }
  const ratio = hit / paths.length;
  console.log(`CDN 命中率 ${(ratio * 100).toFixed(1)}%`);
  if (ratio < 0.9) process.exit(1);   // 低于 90% 让流水线失败，人工介入
}

const paths = (await import('node:fs')).readFileSync(TOP_URLS_FILE, 'utf8').trim().split('\n');
await cdnPrefetch(paths);
await warmAppCaches(paths);
setTimeout(() => verifyHitRatio(paths), 60_000); // 等 CDN 同步后校验
```

## 二十三、弱网与不稳定网络
