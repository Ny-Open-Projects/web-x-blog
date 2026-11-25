---
title: [MFW-164] 笔试：手写一个 Web Vitals 上报 SDK
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-164：笔试：手写一个 Web Vitals 上报 SDK
**答**：实现 `initVitals(options)`：① 用 PerformanceObserver 监听 LCP（`largest-contentful-paint`）；② LCP 取最后一次有效条目（页面停止变化前的最大值）；③ 页面隐藏（visibilitychange → hidden）时上报最终值；④ 上报用 sendBeacon，失败降级 fetch keepalive；⑤ 采样率控制与去重（同一 metric 只上报一次）。

```ts
type VitalsOpts = { endpoint: string; sampleRate?: number; route?: string };

function initVitals({ endpoint, sampleRate = 1, route = location.pathname }: VitalsOpts): void {
  if (Math.random() > sampleRate) return; // 采样门禁

  let lcp: number | null = null;
  let reported = false;                   // 去重：只上报一次

  // ①② LCP 观察：条目可能被更优候选替换，缓存最新值
  try {
    const po = new PerformanceObserver((list) => {
      const entries = list.getEntries();
      const last = entries[entries.length - 1] as PerformanceEntry & { renderTime: number; startTime: number };
      if (last) {
        // renderTime 为 0（跨域资源无 TTFB 信息）时用 startTime 兜底
        lcp = Math.round(last.renderTime || last.startTime);
      }
    });
    po.observe({ type: 'largest-contentful-paint', buffered: true });
  } catch { /* 老浏览器降级：不上报 LCP */ }

  function report(): void {
    if (lcp === null || reported) return;
    reported = true;
    const payload = JSON.stringify({
      metric: 'LCP', value: lcp, route,
      rating: lcp <= 2500 ? 'good' : lcp <= 4000 ? 'ni' : 'poor',
      ts: Date.now(),
    });
    // ④ sendBeacon 优先；失败（队列满/超限 64KB 不会发生但可能被拒）降级 fetch keepalive
    const ok = navigator.sendBeacon?.(endpoint, payload);
    if (!ok) {
      fetch(endpoint, { method: 'POST', body: payload, keepalive: true }).catch(() => {});
    }
  }

  // ③ 页面进入隐藏态 = 用户认为加载完成，上报最终 LCP
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') report();
  }, { once: false });
  // 兜底：unload 前与 10s 后也上报（防止隐藏事件未触发）
  window.addEventListener('pagehide', report);
  setTimeout(report, 10000);
}

export { initVitals };

// 用法：
// initVitals({ endpoint: '/api/vitals', sampleRate: 0.5, route: '/products' });
```

**评分点**：
1. LCP 取「最后一次条目」的机制说对（候替换新，隐藏时定稿）。
2. 上报时机：visibilitychange hidden + pagehide + 超时兜底——只在 unload 上报是错误答案（移动端不可靠）。
3. sendBeacon 失败降级 fetch keepalive，知道 keepalive 的卸载存续语义。
4. 采样与去重（reported 门禁）都有，防止重复打点。
5. rating 阈值符合规范（2.5s/4s），renderTime 为 0 的 startTime 兜底是加分细节。
