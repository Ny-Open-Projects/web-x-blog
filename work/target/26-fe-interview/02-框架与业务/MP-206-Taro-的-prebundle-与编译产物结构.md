---
title: [MP-206] Taro 的编译产物结构与构建管线是什么？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-206：Taro 编译产物结构与构建管线？
**答**：
- 产物：app.js（入口+运行时）、各页面 [page].js（React 组件 + 页面容器）、公共 chunk（vendor）、渲染层 [page].wxml（递归模板）与 .wxss。
- 管线：webpack/vite 打包逻辑层（babel 处理 JSX + Taro 插件注入运行时），渲染层模板是固定资源按需注入（编译时分析用到的组件模板子集——体积优化）。
- 多端差异：编译目标切换平台插件（@tarojs/plugin-platform-weapp/tt/h5…），process.env.TARO_ENV 条件编译。
- 体积控制：运行时核心 ~几十 KB + 按需模板；分包下 vendor 公共化。
- 升级：编译器无关化（Webpack/Vite 双支持）。
