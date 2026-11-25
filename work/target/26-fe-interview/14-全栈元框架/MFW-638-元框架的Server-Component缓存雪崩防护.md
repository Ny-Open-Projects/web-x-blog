---
title: [MFW-638] RSC 的缓存雪崩防护
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-638：RSC 缓存雪崩防护

**答**:
- RSC 缓存雪崩的场景：1) **同 tag 大批失效**（revalidateTag('products') → 1000 个路由同时重渲染——渲染集群打满 RBL-599）；2) **TTL 同时到期**（部署时全部 ISR 页同刻过期——统一 TTL = 雪崩窗口）；3) **冷启动回源**（缓存清空后首流量全量渲染）。
- 防护手段：1) **TTL 抖动**（revalidate = 60 + random(60)——到期时间分散：部署时的统一过期被打散）；2) **失效合并**（同页多次失效一次重渲染 RBL-600 去重）；3) **stale-while-revalidate**（过期立即返回旧值 + 后台重生成——用户无感）；4) **失效限流**（revalidate 队列并发上限 RBL-599 流量加权）。
- 监控：重生成速率（雪崩的信号：重生成 QPS 飙升）+ 渲染延迟（雪崩时 p95 延迟——影响用户的信号）。
- 追问钩子：为什么「TTL 抖动」是最简单却最有效的雪崩防护？——雪崩的根源是「同刻过期」（部署/失效事件的同步性）；抖动 = 60~120s 随机 → 过期分散在 60s 窗口内（重生成速率 = 均匀分摊）；对比 stale-while-revalidate：SWR 保护用户（旧值兜底）但不保护 server（重生成仍集中）——抖动保护 server、SWR 保护用户——两者组合（抖动 + SWR）= 双端防护。

```typescript
// TTL 抖动
function jitteredRevalidate(base: number, { jitterRatio = 0.5 } = {}) {
  return Math.floor(base * (1 + Math.random() * jitterRatio));    // 60 → 60~90s
}
// fetch 时应用
fetch(url, { next: { revalidate: jitteredRevalidate(60) } });
// 部署时的统一过期被打散：重生成速率 = N页 / (60s * jitter) 分摊
// SWR + 抖动组合
export const revalidate = 60;                            // 框架层 SWR 语义（返回旧值后台更新）
// 主动预热（冷启动回源防护）
async function preheat(urls: string[], { concurrency = 20 }) {
  const queue = [...urls];
  await Promise.all(Array.from({ length: concurrency }, async () => {
    while (queue.length) await fetch(origin + queue.shift()).catch(() => {});
  }));
}
// 监控：重生成速率
setInterval(() => {
  const rate = regenCounter.rate();
  if (rate > threshold) alert(`重生成 QPS ${rate}——雪崩信号`);
}, 10000);
```
