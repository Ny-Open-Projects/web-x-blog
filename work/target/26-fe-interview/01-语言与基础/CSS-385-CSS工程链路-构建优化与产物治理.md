---
title: [CSS-385] CSS 工程链路：构建优化与产物治理
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-385：CSS 工程链路：构建优化与产物治理

**答**：
- 构建管线：PostCSS（前缀/降级/polyfill 语法）→ 压缩（cssnano/lightningcss——lightningcss 用 Rust 快 100 倍且内置降级）→ 分包（关键 CSS 提取/路由级 chunk）→ sourcemap
- 产物体积治理：未用规则清除（PurgeCSS/原子化天然按需）、@import 打包合并消灭串行、重复规则去重；体积预算（<50KB gzip 全站）进 CI
- 关键 CSS 提取：首屏样式内联 + 其余异步——工具自动抽取（beasties/critters）按首屏 DOM 计算，注意 SSR 与动态内容的首屏差异
- Polyfill 策略：browserslist 驱动（目标内核决定降级深度），lightningcss 语法降级 + postcss-preset-env 特性 polyfill；:has 降级这类 JS 级 polyfill 按需加载
- 缓存策略：CSS 文件 hash + immutable，与 JS bundle 拆分避免「改一行 JS 全部 CSS 失效」（同 chunk 情况）

```js
// vite 配置要点
export default {
  css: {
    transformer: 'lightningcss',
    lightningcss: { targets: { chrome: 100 << 16 }, browserslist: 'defaults' },
  },
  build: { cssCodeSplit: true, rollupOptions: { output: { /* hash 分包 */ } } },
};
```
