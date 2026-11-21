---
title: [AV-089] CDN 成本与调度概览。
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-089：CDN 成本与调度概览。
**答**：
- 成本模型：带宽计费（按峰值 Mbps 或 95 峰值）或流量计费（GB）；直播成本 ≈ 观看人次 × 观看时长 × 码率，降码率（H265/AV1）与降低高峰峰值直接省钱。
- 调度体系：DNS 调度（粗粒度）+ HTTPDNS（绕劫持、精确到 IP）+ 客户端测速纠偏；多 CDN 之间按质量与成本动态分配流量（成本优先/质量优先模式）。
- 前端配合：探测数据上报（RTT/丢包/首包）、备用域名容灾（主域名 5xx 自动切换）、预热触发（大主播开播前通知预取）。
- 削峰手段：高峰期降默认清晰度、P2P-CDN 混合分发（牺牲部分体验换成本）。
- 核算意识：前端切清晰度策略影响成本——默认档位与 capLevelToPlayerSize 是产品/成本决策不是纯技术决策。

```javascript
// 客户端多 CDN 流量分配执行器（服务端下发权重，客户端按权重选路）
class CdnScheduler {
  constructor() { this.config = null; }
  async refreshConfig() {
    this.config = await fetch('/api/cdn/weights').then((r) => r.json());
    // [{ vendor:'A', domain, weight:0.7 }, { vendor:'B', weight:0.3, backup:true }]
  }
  pick(exclude = []) {
    const pool = this.config.filter((c) => !exclude.includes(c.domain));
    const total = pool.reduce((s, c) => s + c.weight, 0);
    let r = Math.random() * total;
    for (const c of pool) { r -= c.weight; if (r <= 0) return c; }
    return pool[0];
  }
  async fetchWithFailover(path) {
    const tried = [];
    while (tried.length < this.config.length) {
      const cdn = this.pick(tried);
      tried.push(cdn.domain);
      try {
        const res = await fetch(`https://${cdn.domain}${path}`, { signal: AbortSignal.timeout(4000) });
        if (res.ok) return res;
        reportCdnError(cdn.vendor, res.status); // 质量数据回传供调度降权
      } catch (e) { reportCdnError(cdn.vendor, 'timeout'); }
    }
    throw new Error('all cdn failed');
  }
}
```
