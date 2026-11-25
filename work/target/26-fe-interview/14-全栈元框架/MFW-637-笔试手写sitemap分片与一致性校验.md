---
title: [MFW-637] 笔试：手写 sitemap 分片与一致性校验
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-637：笔试：手写 sitemap 一致性校验

**答**：实现 `auditSitemap(sitemapUrls, renderableUrls, lastModMeta)`。renderableUrls: Set（可渲染的 URL——路由清单）；lastModMeta: `Record<url, { dbUpdatedAt: number, sitemapLastmod: number }>`. 规则：1) 死链：sitemap 声明但不可渲染 → finding 'not-renderable'；2) 遗漏：可渲染但未声明（重要页缺失——抓取遗漏）→ finding 'missing'（仅对 priority 高的页——全量遗漏太多噪声）；3) lastmod 漂移：sitemap lastmod 与 DB 更新时间差 > 1h → finding 'stale-lastmod'（爬虫信任）；4) lastmod 恒定不变但 dbUpdatedAt 变了 → 'frozen-lastmod'（构建没更新 meta）；5) 返回 `{ findings: Array<{ url, type }>, health }`（findings 按类型聚合的计数 + health = 'ok'/'degraded'——死链 > 0 即 degraded）。边界：空 sitemap（全遗漏——按可渲染量决定严重度）；lastModMeta 缺（跳过 lastmod 检查）。

```javascript
function auditSitemap(sitemapUrls = [], renderableUrls = new Set(), lastModMeta = {}, { priorityThreshold = 0.8 } = {}) {
  const findings = [];
  const smSet = new Set(sitemapUrls);
  for (const u of sitemapUrls)
    if (!renderableUrls.has(u)) findings.push({ url: u, type: 'not-renderable' });
  for (const u of renderableUrls)
    if (!smSet.has(u) && (lastModMeta[u]?.priority ?? 0.5) >= priorityThreshold)
      findings.push({ url: u, type: 'missing' });
  for (const [u, meta] of Object.entries(lastModMeta)) {
    if (!smSet.has(u)) continue;
    const drift = Math.abs(meta.sitemapLastmod - meta.dbUpdatedAt);
    if (drift > 3600_000) findings.push({ url: u, type: 'stale-lastmod' });
    if (meta.sitemapLastmod === meta.sitemapLastmodPrev && meta.dbUpdatedAt > meta.sitemapLastmodPrev)
      findings.push({ url: u, type: 'frozen-lastmod' });
  }
  const deadCount = findings.filter(f => f.type === 'not-renderable').length;
  return { findings, health: deadCount > 0 ? 'degraded' : 'ok',
    summary: Object.fromEntries(Object.entries(
      findings.reduce((acc, f) => (acc[f.type] = (acc[f.type] || 0) + 1, acc), {}))) };
}

// 自测
const renderable = new Set(['/a', '/b', '/c', '/p/1']);
let r = auditSitemap(['/a', '/b', '/ghost'], renderable, {
  '/a': { dbUpdatedAt: 1000, sitemapLastmod: 1000 },
  '/b': { dbUpdatedAt: 2000, sitemapLastmod: 1500 },       // 漂移 >1h? 假设单位 ms
  '/p/1': { dbUpdatedAt: 3000, sitemapLastmod: 3000, priority: 0.9 },
});
console.log(r.findings.some(f => f.url === '/ghost' && f.type === 'not-renderable'));
console.log(r.health === 'degraded');
console.log(r.summary['not-renderable'] === 1);

// lastmod 漂移（>1h）
r = auditSitemap(['/a'], new Set(['/a']),
  { '/a': { dbUpdatedAt: 1000, sitemapLastmod: 1000 - 7200000 } });
console.log(r.findings.some(f => f.type === 'stale-lastmod'));

// 遗漏（高优先）
r = auditSitemap(['/a'], new Set(['/a', '/hot']),
  { '/hot': { priority: 0.9 } });
console.log(r.findings.some(f => f.url === '/hot' && f.type === 'missing'));

// 低优先遗漏不报
r = auditSitemap(['/a'], new Set(['/a', '/longtail']),
  { '/longtail': { priority: 0.3 } });
console.log(!r.findings.some(f => f.url === '/longtail'));

// 一致
r = auditSitemap(['/a', '/b'], new Set(['/a', '/b']),
  { '/a': { dbUpdatedAt: 1000, sitemapLastmod: 1000 } });
console.log(r.health === 'ok' && r.findings.length === 0);
```

**评分点**：
- 双向对账（sitemap 死链 + 高优页遗漏）；lastmod 漂移与冻结（爬虫信任的两类损伤）
- 遗漏的优先级过滤（噪声控制——只报高优先页）；health 聚合（死链即 degraded）
- 边界（空 sitemap/无 lastmod meta）；summary 计数
- 能说清「sitemap 是与爬虫的契约：死链与乱 lastmod = 信任下降 = 抓取配额缩水」属于加分
