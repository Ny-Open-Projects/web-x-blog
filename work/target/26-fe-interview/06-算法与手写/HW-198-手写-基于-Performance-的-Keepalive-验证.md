---
title: [HW-198] 手写上报通道验证——sendBeacon 返回值/keepalive 限制/64KB 排队检查与降级测试器
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---
## HW-198：手写上报通道验证——sendBeacon 返回值/keepalive 限制/64KB 排队检查与降级测试器
**答**：上报通道的自我验证器（SDK 自监控，PER-246）：sendBeacon 返回 false（64KB 排队满）→ 记录降级事件；fetch keepalive 超 64KB 抛错 → 捕获记录；定期健康探针（小 beacon 到探针端点，服务端回 204 验证链路通）——通道故障时 SDK 降频（防止无效重试堆积）。

```javascript
class ChannelHealth {
  #fails = 0; #lastProbe = 0;
  async send(url, body) {
    const size = new Blob([body]).size;
    if (navigator.sendBeacon?.(url, body)) { this.#fails = 0; return 'beacon'; }
    try {
      const r = await fetch(url, { method: 'POST', body, keepalive: true });
      this.#fails = 0;
      return 'keepalive';
    } catch (e) {
      this.#fails++;
      report({ type: 'channel-fail', size, fails: this.#fails,
               reason: size > 65536 ? 'oversize' : 'network' });      // 超限 vs 网络分开归因
      if (this.#fails >= 5) await this.#probe(url);                   // 连续失败：探针验证链路
      return null;                                                    // 上层静默丢（不无限重试）
    }
  }
  async #probe(url) {                                                 // 链路探针：1KB 小包验证通不通
    const ok = navigator.sendBeacon?.(url + '?probe', new Blob(['ping'], { type: 'text/plain' }));
    if (ok) { this.#fails = 0; report({ type: 'channel-recovered' }); }
    else report({ type: 'channel-down' });                            // 探针也失败：链路断，SDK 降频
  }
}
// 语义：
// sendBeacon false = 排队满（64KB 限制）→ oversize 归因 → SDK 应该拆包（PER-256）不是重试
// keepalive 抛错 = 超 64KB 硬限制 → 同上
// 探针的作用：区分"单包失败（可丢弃）"与"链路断（降频省电）"—— 盲目重试只会堆积
```

**评分点**：
- sendBeacon 返回值检查 + keepalive 64KB 限制的捕获——本题核心。
- oversize vs network 的归因分流（超限该拆包不是重试）。
- 探针机制区分"单包失败"与"链路断"（降频决策）。
- 失败静默丢弃的纪律（PER-251 性能数据允许丢）。
