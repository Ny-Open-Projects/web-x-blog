---
title: [PER-253] CrUX 只测硬导航，SPA 路由切换的体验怎么测？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-253：CrUX 只测硬导航，SPA 路由切换的体验怎么测？

**答**：
- 口径差异：CrUX/CWV 的 LCP/INP 只在**硬导航**（整页加载）上下文收集；SPA 客户端路由切换（pushState）不在标准 CWV 里——用户在站内跳转的"下一页首屏"完全测不到。
- 软导航方案：Chrome 正在推进 SPA soft-nav 的 LCP/INP 扩展（PerformanceObserver 的 `timeOrigin` 变化与 soft-nav entries），可用 `observe({ type: 'soft-nav' })`（或 navigationId 变化检测）作为过渡方案。
- 自定义口径：团队通行的做法是定义 SPNT（Soft Navigation Start → 内容稳定），路由切换后监听 DOM 变更 + rAF 稳定帧判定，近似 LCP 语义。关键是口径写进文档并全站统一。
- 实操建议：主看板仍以硬导航 CWV 为主（可比性），SPA 内导航作为辅助维度（转化路径质量），两者分开验收。

```javascript
// SPA 路由切换首屏近似方案：监听路由 + DOM 稳定
let navStart = 0;
['pushState', 'replaceState'].forEach(fn => {
  const orig = history[fn].bind(history);
  history[fn] = (...args) => { navStart = performance.now(); orig(...args); markSPA(); };
});
addEventListener('popstate', () => { navStart = performance.now(); markSPA(); });

function markSPA() {
  let lastMut = navStart, done = false;
  const mo = new MutationObserver(() => { lastMut = performance.now(); });
  mo.observe(document.body, { childList: true, subtree: true });
  (function check() {
    if (performance.now() - lastMut > 500 && !done) {   // 500ms 无 DOM 变更视为稳定
      report({ type: 'SPA-NT', value: Math.round(lastMut - navStart) });
      done = true; mo.disconnect();
    } else if (!done) requestAnimationFrame(check);
  })();
}
```
