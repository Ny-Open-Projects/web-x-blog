---
title: [OPT-114] Hybrid 容器（App 内 H5）怎么做到"秒开"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-114：Hybrid 容器（App 内 H5）怎么做到"秒开"？

**答**：
- 秒开三板斧：**离线包**（静态资源提前下发到本地，拦截请求走本地文件）、**预渲染/预加载**（进入 App 或点击前就把 WebView 起好、H5 提前 load）、**数据预取**（原生侧提前发首屏接口，H5 起来直接拿结果）。
- 离线包机制：App 启动时拉包清单 -> 差量更新 -> WebView 拦截 `shouldOverrideUrlLoading`（Android）/ `decidePolicyFor`（iOS）映射到本地文件，网络请求归零。
- 预加载时机：首页空闲时预热下一个高频页面的 WebView 实例池（iOS WKWebView 创建就要 100ms+），点进去直接复用。
- 效果衡量：秒开率（1.5s 内可读占比）按渠道统计，未命中场景回捞分析（离线包版本旧？预取失败？）。

```javascript
// 一一对应：Hybrid 侧的离线包拦截 + 预取桥接（以 Android WebView JS 接口示意 + 前端配合）
// 1. 前端与原生约定协议：URL scheme 触发原生预取
function prefetchNextPage(skuId) {
  // 原生拦截该 scheme，提前请求商品接口并缓存
  location.href = `hybrid://prefetch?url=${encodeURIComponent('/api/detail?id=' + skuId)}`;
}

// 2. 原生注入的取数桥：H5 启动时同步拿预取结果（避免二次请求）
// window.HybridBridge.getPrefetched(url) -> string|null（原生内存命中）
async function bootstrap() {
  const url = '/api/detail?id=10086';
  const t0 = performance.now();
  let data = window.HybridBridge?.getPrefetched(url); // 预取命中：0ms 网络
  if (!data) {
    const res = await fetch(url);   // 未命中兜底走网络
    data = await res.text();
  }
  render(JSON.parse(data));
  report('prefetch_hit', {
    hit: !!window.HybridBridge,
    ttfbMs: Math.round(performance.now() - t0),
  });
}

// 3. 前端配合离线包：资源 URL 稳定 + 版本化，包管理器才能精确映射本地文件
// <link rel="stylesheet" href="https://h5.example.com/app.8f2a1c.css" />
// 离线包清单（构建期产出，原生按清单映射）：
// { "https://h5.example.com/app.8f2a1c.css": "offline/20261101/app.css", ... }

// 4. WebView 预热（原生侧逻辑，JS 层仅示意调用）：
// HybridBridge.warmupWebView(); // 首页空闲时预创建 WebView 实例入池
```
