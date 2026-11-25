---
title: [OPT-117] Flutter Web 什么时候该选、什么时候不选？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-117：Flutter Web 什么时候该选、什么时候不选？

**答**：
- Flutter Web 的定位是"同一套代码覆盖 Web"，代价是**自绘引擎**：不走 DOM/CSS，首个渲染慢（下载 engine + 字体 + canvaskit 数 MB）、文本不可选中/SEO 弱、包体与内存高于原生 Web 框架。
- 适合：已有 Flutter App 需要一个低成本的 Web 入口（工具/后台/内嵌面板），交互重度、UI 复杂、SEO 不重要。
- 不适合：内容型网站/电商 C 端（LCP/SEO/可访问性都吃亏），期望"小而快"的营销页。
- 技术要点：渲染器选 `canvaskit`（一致性好，wasm 下载大）vs `html`（体积小但还原差，已进入弃用轨道）；构建用 `--wasm` 减小启动；文本密集页与 SEO 页用原生 Web 技术混排（iframe/微前端分层）。

```bash
# 一一对应：Flutter Web 构建配置与体积/首屏核对
# 1. 生产构建（CanvasKit + WASM，2024 后主推 skwasm）
flutter build web --wasm --release \
  --dart-define=FLUTTER_WEB_CANVASKIT_URL=https://cdn.example.com/canvaskit/ # 引擎放自家 CDN，国内访问 Google CDN 会卡死首屏

# 2. 体积预算检查（构建产物，canvaskit 模式基准）：
# ls -lh build/web/ | awk '{print $5, $9}'
# canvaskit.wasm 约 2-6MB —— 内容型站点用 Flutter Web 前先掂量这笔固定成本
# main.dart.js（AOT 编译产物）随业务增长，用 --analyze-size 定位超大 dart 依赖：
flutter build web --release --analyze-size --target-platform=web-x64

# 3. 首屏核对（用 Lighthouse 跑 Flutter Web 产物）：
# npx lighthouse https://localhost:8080 --preset=desktop --view
# 经验值：TBT/LCP 明显差于同功能 React/Vue 站 —— 若指标是硬约束，选型阶段就应放弃

# 4. 混合方案：SEO 首页用 Next.js，重交互工作台用 Flutter，iframe/web component 嵌入
# flutter build web --wasm --release --base-href /console/
# Next.js 的 /console 路由下 <iframe src="/console/" title="workbench">
```
