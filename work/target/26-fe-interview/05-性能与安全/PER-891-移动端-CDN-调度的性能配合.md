---
title: [PER-891] 移动端 CDN 调度的性能配合：多 CDN 容灾、HTTPDNS 与调度质量度量
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-891：移动端 CDN 调度的性能配合：多 CDN 容灾、HTTPDNS 与调度质量度量

**答**：
- 多 CDN 是移动端常态：单一 CDN 故障（节点劣化/带宽打满）时需要自动切换；调度质量直接决定首屏下载速度。
- 调度手段：HTTPDNS（绕过 LocalDNS 劫持与错误解析，App 内先拿最优 IP 再请求）；CDN 侧按地域/运营商分线路；客户端测速（对各 CDN 下载探测文件选最优）。
- 容灾设计：主 CDN 超时/错误率超阈值 → 自动切备 CDN（请求层重试带备域名）；切换决策要有数据支撑（分 CDN 统计成功率和耗时）。
- 度量：分 CDN 分域名的下载耗时 p75、失败率、HTTPDNS 命中率与解析耗时；劣化告警驱动调度策略调整。

```javascript
const cdnDispatch = {
  candidates: ['cdn-a.example.com', 'cdn-b.example.com'],
  async pick(url) {
    const ip = await httpdns.lookup(url);                      // HTTPDNS 优先解析
    const best = await probeFastest(this.candidates);          // 客户端测速选路
    report('cdn-pick', { best, dns: ip ? 'httpdns' : 'local' });
    return best;
  },
  async fetchWithFailover(path) {
    for (const host of this.candidates) {                      // 容灾重试
      try {
        const r = await fetch(`https://${host}${path}`, { signal: AbortSignal.timeout(3000) });
        if (!r.ok) throw new Error(r.status);
        recordCdnStat(host, { ok: true });
        return r;
      } catch (e) { recordCdnStat(host, { ok: false }); }
    }
    throw new Error('all-cdn-failed');
  },
};
```
