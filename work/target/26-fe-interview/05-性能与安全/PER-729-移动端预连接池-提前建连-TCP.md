---
title: [PER-729] 移动端预连接池：提前建连 TCP/TLS 的时机、数量与回收策略怎么设计？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-729：移动端预连接池：提前建连 TCP/TLS 的时机、数量与回收策略怎么设计？

**答**：
- 场景：进入首页后空闲时预建到 API 域/图片域的连接（TCP+TLS 握手 100~300ms），用户点击后直接复用；手段 `preconnect`（声明式）或 fetch 一个极小资源（主动建连）。
- 要点：时机在首屏渲染完成后（idle），不抢首屏带宽；数量收敛（同域 HTTP/2 复用连接，预连 2~3 个域即可，多域预连反而耗电）；DNS 预解析（dns-prefetch）比全量 preconnect 更便宜，分两档使用。
- 边界：预建连接有超时（30~60s 不用就关），复用率低于 50% 应收缩清单；iOS 低电量模式会限制预连接（检测后跳过）。
- 评分点：分档预连与复用率回收。

```javascript

class PreconnectPool {
  constructor(domains, { max = 3 } = {}) {
    this.domains = domains.slice(0, max);                       // 域收敛：最多 3 个
    this.hits = 0; this.uses = 0;
  }
  warm() {                                                      // 首屏后 idle 预建
    if (navigator.getBattery?.then) return;                     // 低电量模式跳过
    (window.requestIdleCallback ?? setTimeout)(() => {
      this.domains.forEach(d => {
        const link = document.createElement('link');
        link.rel = 'preconnect'; link.href = `https://${d}`; link.crossOrigin = 'anonymous';
        document.head.appendChild(link);
        this.pending = new Set(this.domains);
      });
    }, { timeout: 2000 });
  }
  onUse(domain) {                                               // 复用率统计
    this.uses++;
    if (this.pending?.delete(domain)) this.hits++;
  }
  report() {                                                    // 复用率 < 50% 收缩清单
    const rate = this.uses ? this.hits / this.uses : 0;
    if (rate < 0.5) this.domains = this.domains.slice(0, 1);    // 收缩
    return { hitRate: +(rate * 100).toFixed(0) + '%', domains: this.domains };
  }
}
// 两档使用：dns-prefetch 便宜可多配；preconnect 昂贵只给核心 API/图片域
```
