---
title: [V3-322] 如何在现有工程灰度启用 Vapor 模式？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-322：如何在现有工程灰度启用 Vapor 模式？
**答**：
- 配置入口：vite 插件 `@vue-macros/vapor` 或 Vue 官方实验支持里给 SFC 加 `vapor` 特性/编译开关，按文件或目录启用，未启用的继续走 VDOM。
- 灰度顺序：先叶子组件（展示型、交互简单）→ 列表/表单组件 → 路由级页面；每步用 e2e 回归。
- 验收指标：交互吞吐（setState→DOM 更新耗时）、内存、bundle 体积三项对比基线。
- 回退方案：开关按页面维度下发（配置中心），异常页一键切回 VDOM 构建。
- 注意团队成本：Vapor 心智（无 vnode）与调试工具链仍在完善，团队需同步踩坑文档。
```javascript
// vite.config.ts
import vue from '@vitejs/plugin-vue'
export default { plugins: [vue({ features: { vapor: true } })] } // 实验性，按 SFC 粒度启用
```
