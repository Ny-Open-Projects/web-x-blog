---
title: [WEB-255] 首屏白屏排查 SOP
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 排查]
type: 面试题
---

## WEB-255：首屏白屏排查 SOP

**答**：
- 先定位层次：全白（连 HTML 都没到）→ 网络/DNS/CDN 问题；HTML 到了但无内容 → JS 执行/接口问题。
- 全白检查链：用户端网络（弱网/DoH）→ DNS 解析 → CDN 节点（X-Cache、刷新）→ 源站 nginx 日志 → HTTPS 证书过期。
- HTML 正常时查：Console 报错（JS 语法/模块加载失败/白屏脚本在 head 阻塞）→ Network（JS bundle 404：发版时序不一致，旧 HTML 引用已删除的 hash 文件）→ 接口状态（核心接口 5xx/超时，页面依赖接口渲染）。
- 系统化手段：打点上报白屏（DOM 采样检测 + window.onerror 关联）、灰度回滚开关、本地复现用 lighthouse/低网速模拟。
- 预防：HTML 不缓存 + 静态资源非覆盖式保留至少 N 个版本、错误监控覆盖 script error、发版后自动化冒烟。

```javascript
// 白屏检测上报（简化版）
new PerformanceObserver((list) => {
  const { renderTime } = list.getEntries().pop(); // LCP
  if (!renderTime) return;
  setTimeout(() => {
    const root = document.querySelector('#app');
    const blank = !root || root.children.length === 0;
    if (blank || renderTime > 5000) {
      navigator.sendBeacon('/report/blank', JSON.stringify({
        url: location.href, blank, lcp: renderTime,
        ua: navigator.userAgent, ts: Date.now(),
      }));
    }
  }, 3000);
}).observe({ type: 'largest-contentful-paint', buffered: true });
```
