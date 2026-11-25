---
title: [CSS-382] 样式热更新与 HMR 的失效面：开发体验深水
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-382：样式热更新与 HMR 的失效面：开发体验深水

**答**：
- CSS HMR 原理：Vite/webpack 监听样式文件变化 → 重新编译 → 替换 <style> 内容或 link href——不刷新页面（保留组件状态），这是 CSS HMR 的核心价值
- 替换语义：整文件替换使该文件全部规则失效重算（开发期可接受）；CSS Modules 的类名 hash 变化会导致「旧 class 残留」（动态拼接类名的组件要整页刷新兜底）
- Tailwind JIT 与 HMR：内容扫描重跑 + 原子类重新生成——增量场景快，首次/配置变化慢；uno/tailwind 的 safelist 处理动态类名
- 状态保持边界：CSS 变量主题（运行时切换的 data-theme）在 HMR 后保留（属性在 DOM 上）；但「JS 注入的样式」（styled-components）HMR 后组件重挂载主题丢失——开发期主题丢失是高频困扰
- 源码映射与调试：sourceMap 把编译后 CSS 映射回源文件（sass/less/postcss 链路都要传 sourceMap 才能准确断点）

```javascript
// vite CSS HMR 边界兜底
if (import.meta.hot) {
  import.meta.hot.accept(() => location.reload());  // 类名 hash 变化时整刷
}
// styled-components 主题丢失兜底: themeProvider 状态外置 sessionStorage
```
