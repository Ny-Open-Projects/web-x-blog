---
title: [PER-744] 手写一个 Speculation Rules 预渲染管理器：按用户意图配置 prerender/prefetch 并统计命中收益
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-744：手写一个 Speculation Rules 预渲染管理器：按用户意图配置 prerender/prefetch 并统计命中收益

**答**：
- Speculation Rules API（Chrome 109+）：JSON 配置声明 `prefetch`（预取文档）与 `prerender`（完整预渲染下一页）；移动端收益巨大（点击即成品页面，省 300ms~1s）。
- 实现：script[type=speculationrules] 动态注入，规则来源：静态（导航主链接）+ 动态（漏斗 TopN 路由）；eagerness 分档（eager 预渲染 / moderate 鼠标悬停/触摸开始预取）；命中统计（prerender 页面 activation 与直接加载区分——`document.prerendering` / activationStart）。
- 要点：prerender 页面要预渲染安全"（无副作用：不发 POST、不播音频、不清购物车——页面代码要守卫 prerendering 状态）；预渲染数量预算（同站 2~3 个）。
- 边界：不支持的浏览器降级 preconnect/prefetch；内存压力下浏览器自动丢弃 prerender（要容忍不命中）。
- 评分点：prerender 安全守卫与 activation 计量。

```javascript

function installSpeculation(candidates) {
  const supported = HTMLScriptElement.supports?.('speculationrules');
  if (!supported) return fallbackPrefetch(candidates);          // 降级 preconnect
  const rules = {
    prerender: [{ where: { href_matches: candidates.map(c => `${c}/*`) },
      eagerness: 'moderate' }],                                 // moderate：交互意图才触发
    prefetch: [{ where: { href_matches: candidates.map(c => `${c}/*`) },
      eagerness: 'eager' }],
  };
  const s = document.createElement('script');
  s.type = 'speculationrules';
  s.textContent = JSON.stringify(rules);
  document.head.appendChild(s);
}
// 页面侧守卫：预渲染阶段不做副作用
if (document.prerendering) {
  pauseAnalytics(); pauseVideoAutoPlay();                       // 不发统计不播视频
  document.addEventListener('prerenderingchange', () => {
    resumeAnalytics();                                          // activation 时恢复
    report('prerender-activated', { delayMs: performance.now() - performance.activationStart });
  }, { once: true });
}
function fallbackPrefetch(routes) {
  routes.forEach(r => { const l = document.createElement('link');
    l.rel = 'prefetch'; l.href = r; document.head.appendChild(l); });
}
```
