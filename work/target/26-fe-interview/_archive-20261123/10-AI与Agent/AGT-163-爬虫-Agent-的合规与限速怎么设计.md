---
title: [AGT-163] 爬虫 Agent 的合规与限速怎么设计？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-163：爬虫 Agent 的合规与限速怎么设计？
**答**：
- 合规三查：robots.txt 与站点 ToS 解析前置（禁止抓取的路径直接进黑名单）、版权与个人信息过滤（抓取内容入知识库前过 PII/版权标记）、数据驻留约束（跨地区站点数据落哪个区）。
- 限速令牌桶：按域名维度限速（如每域名 1 req/s），全局限速叠加；遇 429/Retry-Header 退避并把该域降速；夜间低峰调度大批量任务。
- 礼貌性协议：设置真实 UA 与联系邮箱、遵守 ETag/If-Modified-Since 条件请求减少重复抓取、并发连接数限制。
- Agent 特有风险：爬到的网页内容会进 prompt（注入风险，配合 AGT-123 的扫描）；抓取目标由模型动态决定时，目标必须过白名单域名校验，防止被诱导爬内网地址（SSRF）。

```typescript
// 爬虫 Agent：域白名单 + 令牌桶限速 + robots 校验
import { z } from 'zod';

const TargetUrl = z.string().url();

export class PolitenessLimiter {
  private buckets = new Map<string, { tokens: number; last: number }>();
  constructor(private perDomainRps = 1, private globalRps = 20) {}

  async acquire(url: string): Promise<void> {
    const domain = new URL(url).hostname;
    await this.take(domain, this.perDomainRps);
    await this.take('__global__', this.globalRps);
  }
  private async take(key: string, rps: number) {
    for (;;) {
      const b = this.buckets.get(key) ?? { tokens: rps, last: Date.now() };
      const now = Date.now();
      b.tokens = Math.min(rps, b.tokens + ((now - b.last) / 1000) * rps);
      b.last = now;
      if (b.tokens >= 1) { b.tokens -= 1; this.buckets.set(key, b); return; }
      await new Promise((r) => setTimeout(r, ((1 - b.tokens) / rps) * 1000));
    }
  }
}

export async function agentCrawl(url: string, limiter: PolitenessLimiter, whitelist: string[]) {
  const target = TargetUrl.parse(url);
  const domain = new URL(target).hostname;
  if (!whitelist.includes(domain)) throw new Error(`目标域名不在白名单：${domain}`);   // 防 SSRF 与越权爬取
  if (/(^|\.)internal\.corp$/.test(domain) || !/^https:/.test(target)) throw new Error('仅允许 https 公网白名单域');

  const robots = await fetch(`https://${domain}/robots.txt`).then((r) => r.text());
  if (disallowedFor(robots, target.pathname)) { metrics.inc('crawl.robots.blocked'); return null; }

  await limiter.acquire(target);
  const res = await fetch(target, { headers: { 'User-Agent': 'CorpResearchBot/1.0 (+https://corp.example/bot)' } });
  if (res.status === 429) { const ra = Number(res.headers.get('retry-after') ?? 60); await sleep(ra * 1000); return agentCrawl(url, limiter, whitelist); }
  const html = await res.text();
  return injectScan(htmlToText(html));   // 内容进 prompt 前过注入扫描（AGT-123）
}

function disallowedFor(robots: string, path: string): boolean {
  return robots.split('\n').some((l) => l.startsWith('Disallow:') && path.startsWith(l.split(':')[1]?.trim() ?? '\u0000'));
}
function htmlToText(html: string) { return html.replace(/<[^>]+>/g, ' '); }
function injectScan(text: string) { return text; }
function sleep(ms: number) { return new Promise((r) => setTimeout(r, ms)); }
const metrics = { inc: (n: string) => { void n; } };
```
