---
title: [ARC-082] SDK 的体积与加载策略如何设计（按需初始化/延迟加载）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-082：SDK 的体积与加载策略如何设计（按需初始化/延迟加载）？
**答**：
- 分层加载：核心（采集+上报，<15KB gzip，同步引入）、增强模块（录屏/APM 细节，动态 import 按需拉）、重型依赖（压缩库等，首次使用时加载）。
- 初始化时机：错误监控最早（页面 head 内联 loader）、性能/行为监控 idle 后初始化、非关键 SDK 交互触发后加载。
- 度量：SDK 自身的加载/初始化耗时纳入采集（吃自己的狗粮），包体积进 CI 门禁（size-limit）。

```typescript
// 分层加载编排
export function initMonitor(config: Config) {
  const core = new MonitorCore(config);           // 核心：同步加载，尽早捕获错误
  core.install(errorPlugin, pluginPv);
  // 增强能力：idle 后动态 import，不占首屏预算
  requestIdleCallback(async () => {
    if (config.features?.replay) {
      const { replayPlugin } = await import(/* webpackChunkName: "replay" */ './plugins/replay');
      core.install(replayPlugin({ maskAllInputs: true }));   // 重型能力懒加载
    }
  });
  // 业务触发加载：用户开启某功能才拉对应插件
  window.addEventListener('corp:debug-mode', async () => {
    const { debugPlugin } = await import('./plugins/debug');
    core.install(debugPlugin);
  });
  return core;
}
// CI 门禁：
// "size-limit": [ { "path": "dist/core.js", "limit": "15 kb" },
//                 { "path": "dist/replay.js", "limit": "60 kb" } ]
```
