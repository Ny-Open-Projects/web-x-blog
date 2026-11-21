---
title: [SCN-095] 首屏接入埋点、客服、统计、AB 测试 4 个第三方脚本，拖慢 LCP，如何治理？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-095：首屏接入埋点、客服、统计、AB 测试 4 个第三方脚本，拖慢 LCP，如何治理？
**答**：
- 分优先级处置：埋点/统计/客服都不是首屏必需，移到 window load 后 requestIdleCallback 注入，不与首屏资源抢带宽；加载失败静默降级。
- AB 分流逻辑必须首帧前生效（防闪烁），但分流算法本地化（确定性哈希），不依赖远程接口，兼顾正确性与速度。
- 能替换就替换：重 SDK 同步脚本改自建轻量上报或服务端收数，从源头减少第三方体积。

```javascript
// 第三方脚本延迟化：非关键 SDK 空闲时加载 + AB 分流本地化
function idleLoad(src) {
  return new Promise((resolve, reject) => {
    const run = () => {
      const s = document.createElement('script');
      s.src = src; s.async = true;
      s.onload = resolve; s.onerror = reject;
      document.head.appendChild(s);
    };
    // load 后且浏览器空闲再加载，失败不影响主流程
    window.addEventListener('load', () =>
      'requestIdleCallback' in window
        ? requestIdleCallback(run, { timeout: 5000 })
        : setTimeout(run, 3000));
  });
}
idleLoad('https://sdk.analytics.com/analytics.js').catch(() => {});

// AB 分流本地化：确定性哈希，首帧前即可生效，无远程依赖无闪烁
function bucket(userId, experiment, ratio = [0.5, 0.5]) {
  let h = 0;
  for (const c of `${experiment}:${userId}`) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  const slot = (h % 1000) / 1000;
  let acc = 0;
  for (let i = 0; i < ratio.length; i++) {
    acc += ratio[i];
    if (slot < acc) return i;   // 同一用户永远同一组
  }
  return ratio.length - 1;
}
```
