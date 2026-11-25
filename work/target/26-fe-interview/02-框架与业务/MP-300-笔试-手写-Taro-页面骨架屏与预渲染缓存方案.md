---
title: [MP-300] 笔试：手写启动优化组合（骨架屏 + 初始渲染缓存 + 预加载）方案落地
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 笔试题, 19]
type: 笔试题
---

## MP-300：笔试：手写启动优化组合方案
**答**：落地「首页启动优化」：① app.json 开启 initialRenderingCache；② 页面首屏骨架（静态结构在缓存中呈现）+ 数据并行拉取；③ 关键分包 preloadRule；④ 按需注入 lazyCodeLoading；⑤ 优化效果验证方案（指标与对照）。写出关键配置与页面结构。

```json
// app.json
{
  "lazyCodeLoading": "requiredComponents",
  "preloadRule": { "pages/index/index": { "network": "all", "packages": ["pkgGoods"] } }
}
```

```javascript
// pages/index/index.json
// { "initialRenderingCache": "static" }
// 页面结构：静态骨架进入渲染缓存，数据到后 setData 替换
Page({
  data: { goodsList: [], skeleton: true },
  onLoad() {
    // 数据并行：骨架已由渲染缓存先出，这里只等数据
    Promise.all([api.getGoodsList(), api.getBanners()]).then(([list, banners]) => {
      this.setData({ goodsList: list, banners, skeleton: false }) // 一次性替换
    }).catch(() => this.setData({ skeleton: false, loadError: true }))
  }
})
```

**验证方案**：
- 指标：appLaunch→homeReady P95（getPerformance + 自研打点）、首屏 setData 量、分包页白屏时长。
- 对照：优化前版本灰度 10% 流量双跑一周，对比启动耗时分布。
- 回归门禁：CI 构建产物体积与启动打点冒烟。

**评分点**：
- 五项配置齐全且理解各自作用（缓存/预下载/按需注入/骨架/数据并行）。
- 一次性 setData 替换（减少消息次数）。
- 验证方案包含灰度对照与指标定义。
- 能说出 initialRenderingCache 的失效边界（结构变更）。
