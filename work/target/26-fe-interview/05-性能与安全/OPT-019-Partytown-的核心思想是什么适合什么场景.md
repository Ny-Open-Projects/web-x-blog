---
title: [OPT-019] Partytown 的核心思想是什么？适合什么场景？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-019：Partytown 的核心思想是什么？适合什么场景？

**答**：
- Partytown 把第三方分析/营销脚本从主线程搬进 **Web Worker** 执行，让第三方代码不再抢占主线程。
- 技术关键：Worker 里没有 DOM，Partytown 通过同步消息代理（Synchronous XHR 风格的 service worker 桥）拦截 `document/window` 访问，转发回主线程执行，让第三方脚本"以为"自己能直接碰 DOM。
- 适合：GA、GTM、Facebook Pixel、Hotjar 等纯数据收集类脚本；不适合需要真实渲染的脚本（如聊天挂件 UI、地图）。
- 集成成本极低：一个 script + `type="text/partytown"` 标记要迁移的脚本。

```html
<!-- 一一对应：Partytown 集成，把 GA 脚本移入 Worker -->
<!-- 1. 在页面头部引入 partytown 的 snippet -->
<script>
  partytown = {
    forward: ['dataLayer.push'], // 转发 dataLayer 调用到 worker
  };
</script>
<script src="/~partytown/debug/partytown.js"></script>

<!-- 2. 原 GA 脚本加上 type="text/partytown"，主线程不再执行它 -->
<script type="text/partytown">
  (function (i, s, o, g) {
    i['GoogleAnalyticsObject'] = o;
    i[o] = i[o] || function () { (i[o].q = i[o].q || []).push(arguments); };
    i[o].l = 1 * new Date();
    i[o].src = g;
    document.head.appendChild(i[o]);
  })(window, document, 'ga', 'https://www.google-analytics.com/analytics.js');
  ga('create', 'UA-XXXXX-Y', 'auto');
  ga('send', 'pageview');
</script>
```

## 四、接口与数据层优化
