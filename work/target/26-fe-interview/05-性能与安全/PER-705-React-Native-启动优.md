---
title: [PER-705] React Native 启动优化：Hermes 字节码、懒加载与启动任务分级怎么排？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-705：React Native 启动优化：Hermes 字节码、懒加载与启动任务分级怎么排？

**答**：
- Hermes 字节码：预编译字节码跳过 JS 解析（启动快 30%+），且内存峰值更低；开启 `hermesEnabled` 并验证产物为 .hbc；字节码预热（mmap 页缓存）。
- 启动任务分级：**必须同步**（导航容器/全局 Provider 最小集）、**可交互后**（非首屏组件/统计 SDK）、**空闲时**（预加载下一页/清理任务）——用 InteractionManager + IdleCallbacks 排队。
- JS bundle 拆分：基础包 + 业务包（增量更新场景），或按 Tab 懒渲染（首屏只渲染第一个 Tab）。
- 度量：启动分段（native init -> JS bundle load -> 首帧 -> 可交互），用 React DevTools Profiler + native 启动埋点；优化目标低端机冷启 < 2s。

```javascript

const rnStartupPlan = {
  hermes: { enable: 'hermesEnabled=true', verify: '产物 .hbc 字节码', gain: '启动 -30%，内存峰值更低' },
  taskTiers: {
    sync: ['导航容器', '全局 Provider 最小集'],
    afterInteract: ['非首屏 Tab', '统计 SDK', '推送注册'],
    idle: ['下一页预取', '日志清理'],
  },
  bundle: { split: '基础包+业务包', lazyTab: '首屏只渲染第一个 Tab' },
  metrics: ['native init -> bundle load -> 首帧 -> 可交互 分段', '低端机冷启 < 2s'],
};
// 任务分级实现：InteractionManager.runAfterInteractions(() => loadAfterInteract());
// requestIdleCallback(() => loadIdleTasks());
```
