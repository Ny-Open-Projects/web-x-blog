---
title: [PER-091] BFCache 的启用条件是什么？如何排查与利用？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-091：BFCache 的启用条件是什么？如何排查与利用？

**答**：
- BFCache（往返缓存）：后退/前进时浏览器直接恢复整页内存快照，导航耗时接近 0；触发条件苛刻，**任何一环不满足即失效**。
- 常见失效源：`unload`/`beforeunload` 监听（最大杀手）、`Cache-Control: no-store`、HTTPS 证书问题、打开 WebSocket、`opener` 存在（跨窗引用）、部分 iframe/权限请求。
- 排查工具：Chrome DevTools 的 Back/forward cache 面板直接给出“为什么不能用”的原因列表；线上用 `pageshow` 的 `event.persisted` 统计命中率。
- 复活处理：BFCache 恢复的页面 JS 状态是旧的，要在 `pageshow` 里刷新时效性数据（token、库存），并重连 WebSocket。

```javascript
// BFCache 兼容三件事：不阻塞、能感知、复活后刷新
// 1) 禁用 unload —— 用 pagehide 替代，unload 会直接禁用 BFCache
window.addEventListener('pagehide', (e) => {
  if (!e.persisted) navigator.sendBeacon('/api/leave', '{}'); // 真离开才上报
});

// 2) pageshow 感知 BFCache 恢复，统计线上命中率
window.addEventListener('pageshow', (e) => {
  if (e.persisted) {
    // 3) 复活后刷新时效性数据：快照里的 token/库存可能已过期
    Promise.all([
      fetch('/api/me', { credentials: 'include' }),
      fetch('/api/cart/count', { credentials: 'include' }),
    ]).then(([me, cart]) => {
      if (me.status === 401) location.assign('/login'); // 快照期间登录态失效
      updateCartBadge(cart.count);
    });
    reconnectWebSocket(); // 快照里的 WS 已断，必须重连
  }
});
```

```nginx
# nginx：不要对 HTML 下发 no-store（会禁用 BFCache），改用协商缓存
location = /index.html {
    add_header Cache-Control "no-cache"; # 必须回源验证，但允许 BFCache
    proxy_pass http://app;
}
```

## 十五、运行时性能深水区

本章把运行时优化从“排查单点”升级为“系统性方案”：内存分配模式、合成器友好渲染、输入链路、监控降级四条线，共同原则是**让主线程做最少的事，把能下放的计算交给 Worker/合成器**。先给一个全章通用的基线工具，后文各题都可用它量化收益。

```javascript
// 本章通用的性能护栏：任何运行时方案上线前先建基线
function baseline(name, setup, run, times = 100) {
  setup();
  const samples = [];
  for (let i = 0; i < times; i++) {
    const t0 = performance.now();
    run();
    samples.push(performance.now() - t0);
  }
  samples.sort((a, b) => a - b);
  console.log(name, {
    p50: samples[Math.floor(times * 0.5)].toFixed(2),
    p95: samples[Math.floor(times * 0.95)].toFixed(2),
  });
  return samples;
}
```
