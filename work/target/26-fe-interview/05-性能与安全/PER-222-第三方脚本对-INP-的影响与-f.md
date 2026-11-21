---
title: [PER-222] 第三方脚本如何拖慢 INP？facade 模式与 worker 化隔离怎么做？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-222：第三方脚本如何拖慢 INP？facade 模式与 worker 化隔离怎么做？

**答**：
- 拖慢路径：三方 SDK 常在全局监听 scroll/pointer 等高频事件做埋点、做主线程计算（AB 分流、个性化推荐）、同步读写 DOM（聊天挂件）——每次用户交互它们都要插一脚，input delay 与 processing 段同时被拉长。
- facade 模式：对重资源交互组件（YouTube/地图/客服气泡）默认渲染轻量静态替身（封面图 + 播放按钮），用户点击时才动态加载真实 SDK。视频/地图场景可省 500KB+ JS 与数秒主线程占用。
- worker 化隔离：把纯计算类三方（统计聚合、AB 分桶）移入 Web Worker，与主线程零竞争；无法改造的 SDK 用 Partytown 类方案把第三方脚本整体搬进 worker 线程执行（通过同步代理桥接 DOM API）。
- 治理配套：三方脚本统一走自研加载器（defer、idle 加载、超时熔断），CI 卡口限制三方请求数与体积，监控按 invoker 归因持续追责。

```html
<!-- facade：YouTube 视频先渲染 8KB 替身，点击才拉真实 iframe（省 ~1MB JS） -->
<div class="video-facade" data-video="dQw4w9WgXcQ">
  <img src="/cover/dQw4w9WgXcQ.avif" width="560" height="315" alt="播放视频">
  <button aria-label="播放">▶</button>
</div>
<script>
document.querySelector('.video-facade').addEventListener('click', (e) => {
  const id = e.currentTarget.dataset.video;                 // 用户主动点击后才加载
  e.currentTarget.outerHTML =
    `<iframe width="560" height="315" loading="lazy"
       src="https://www.youtube.com/embed/${id}?autoplay=1"
       title="视频" allowfullscreen></iframe>`;
}, { once: true });
</script>
```
