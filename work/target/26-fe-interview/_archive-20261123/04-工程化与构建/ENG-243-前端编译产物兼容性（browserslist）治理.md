---
title: [ENG-243] 编译产物兼容性（browserslist/polyfill）治理怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-243：兼容性治理怎么做？
**答**：
- 单源目标：browserslist 配置全仓单源（共享包），构建/PostCSS/polyfill 全部消费同一目标——目标不一致是「一个浏览器这里好那里坏」的根源。
- 数据驱动：按真实用户浏览器分布（RUM 统计）定目标，而不是通配「最近 2 版」——流量 99% 集中在 8 个版本时，为 2% 老浏览器付的 polyfill 体积要重新评估。
- polyfill 策略：core-js 按需注入（useBuiltIns: usage）+ 差异化服务（老浏览器独立产物或提示升级），默认产物不带全量 polyfill。
- 兼容性回归：目标浏览器矩阵进 E2E 网格（至少 iOS Safari/Android WebView 低版本各一）。
- 追问钩子：为什么目标要用自家 RUM 数据而不用 caniuse 默认——caniuse 是全球数据，你的用户分布（如东南亚 Chrome 低版本多/政务 IE 残留）可能天差地别；兼容性决策唯一可信输入是自己的流量分布。

```jsonc
// 单源 browserslist（@org/config 包）
{ "browserslist": ["> 0.5%", "iOS >= 14", "Android >= 9", "not dead"] }
```
```javascript
// vite/webpack: useBuiltIns: 'usage', corejs: 3
// RUM 驱动复核
rumBrowserDistribution() // -> 每季度回顾 targets 是否合理
```
