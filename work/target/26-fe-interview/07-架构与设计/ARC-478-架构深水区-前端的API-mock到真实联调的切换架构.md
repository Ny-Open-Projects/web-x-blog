---
title: [ARC-478] 从 Mock 到真实联调的切换架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-478：从 Mock 到真实联调的切换架构
**答**:
- 切换架构目标：同一份代码不改业务逻辑，通过环境层切换数据源（本地 mock / 测试环境 / 真实环境），切换点收敛在请求层与配置层。
- 实现收口：请求层按 dataMode 决定走 MSW 拦截（ARC-366）还是真实网关；dataMode 由环境配置驱动（本地默认 mock、联调分支可切真实）；业务代码不感知。
- 部分切换：联调期常见"接口 A 就绪、接口 B 未完成"——按接口粒度开关（mock 白名单），就绪一个切一个；契约测试保证切真实后行为与 mock 一致。
- 联调期观测：切换率面板（mock 接口占比随联调进度下降曲线），全量真实即联调完成标志。
- 风险防：mock 与真实契约漂移——schema 单源生成 mock（ARC-366），契约测试 CI 里每日跑真实环境比对。
```javascript
// 数据源切换层
const dataMode = env.DATA_MODE; // 'mock' | 'hybrid' | 'live'
function setupDataLayer() {
  if (dataMode === 'mock') return startWorker(allHandlers);
  if (dataMode === 'hybrid')
    return startWorker(allHandlers.filter(h => !readyMocks.has(h.path))); // 就绪接口走真实
  // live: 无 SW 拦截，直连网关
}
```
