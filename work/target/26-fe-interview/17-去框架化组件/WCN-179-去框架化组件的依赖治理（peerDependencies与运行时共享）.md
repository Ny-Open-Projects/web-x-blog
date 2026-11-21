---
title: [WCN-179] 去框架化组件的依赖治理：共享 runtime 单例、peerDependencies 与 importmap 怎么协同？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-179：去框架化组件的依赖治理：共享 runtime 单例怎么协同？

**答**：
- 问题：组件库依赖 signals-core/Lit runtime，多宿主或多组件版本各打一份 → 内存与通信割裂（两个 store 实例）、体积翻倍。
- 方案一（npm 宿主）：runtime 声明为 peerDependencies + 宿主 bundler externals → 全站单份；CI 校验 peer 版本区间。
- 方案二（CDN 场景）：importmap 集中映射 runtime URL，组件 import '@acme/signals-core' 走映射；宿主一次加载全站共享。
- 方案三（强隔离需求）：故意双份（版本共存期）——store 不互通是接受的代价，用 window 级桥接做过渡同步。
- 校验手段：运行时检测——组件初始化时 `window.__ACME_SIGNALS__ ??= signalsCore` 幂等挂载，多实例出现时 console.warn（诊断信息：几个实例、来自哪些组件版本）。
- 升级策略：runtime 语义化版本 + 组件 peer 区间宽松（^1.0.0）；major 升级走双实例共存窗口。

```javascript
// 组件入口：runtime 单例幂等挂载
import * as signalsCore from '@acme/signals-core';

if (window.__ACME_SIGNALS__ && window.__ACME_SIGNALS__ !== signalsCore) {
  console.warn('检测到多份 signals-core 实例：请检查 importmap/externals 配置');
}
window.__ACME_SIGNALS__ ??= signalsCore;
```
