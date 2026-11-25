---
title: [MP-245] WebView 与 Skyline 渲染的实测对比怎么做？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-245：WebView vs Skyline 实测对比？
**答**：
- 测试矩阵：同页面双 renderer 构建（app.json 按页配置），关键指标——首屏 setData→渲染完成、滚动帧率（复现长列表/动图）、手势响应延迟、内存峰值。
- 工具：真机（iOS/Android 各 3 机型）+ 微信开发者工具真机调试 + perf 面板；自动化用 miniprogram-automator 触发滚动并录制。
- 典型结果：Skyline 长列表滚动与动画帧率显著优（无 WebView 合成层开销）；复杂 CSS 页面 Skyline 兼容裁剪需改造。
- 输出：分页面的 renderer 决策表 + 迁移工时评估。
- 注意版本依赖：Skyline 基础库版本要求（≥3.x），低版本用户回退 WebView。
