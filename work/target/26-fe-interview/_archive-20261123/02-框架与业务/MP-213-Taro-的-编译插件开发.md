---
title: [MP-213] 怎么开发一个 Taro 编译插件？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-213：Taro 编译插件开发？
**答**：
- 插件形态：NPM 包导出 Taro 插件（ctx.onBuildStart/onModifyWebpackConfig/ctx.onCompilerMake 等钩子）。
- 典型用途：自定义平台（plugin-platform-xxx 定义模板/组件映射/API 垫片）、构建注入（环境变量/依赖替换）、产物后处理（尺寸分析）。
- Webpack 层：modifyWebpackConfig 里加 loader/plugin（如自动埋点 babel 插件）。
- 模板定制：新增端的渲染模板（template 混合）。
- 生命周期：构建/编译/生产 hook 时序要查当前 Taro 版本 API——版本间差异是主要坑。
