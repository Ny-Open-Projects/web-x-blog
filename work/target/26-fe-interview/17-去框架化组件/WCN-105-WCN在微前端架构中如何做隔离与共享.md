---
title: [WCN-105] WCN 在微前端架构中如何做隔离与共享？（Shadow DOM 隔离、依赖外置、store 共享）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-105：WCN 在微前端架构中如何做隔离与共享？（Shadow DOM 隔离、依赖外置、store 共享）

**答**：
- 隔离层：Shadow DOM 提供 DOM/样式隔离；tag 命名空间（前缀 + 版本）防 define 冲突；子应用的组件 bundle 用 import map 或 externals 复用主应用的共享依赖（Vue/React 单实例）。
- 共享层：跨子应用业务状态用"主应用提供的 Signals store 单例"——以 window.__共享 或 npm 包 external 方式保证只有一个实例；主题 token 从主应用 CSS 变量继承穿透影子树。
- 生命周期：子应用挂载时 define 自己的组件、卸载时不能"undefine"（标准不支持）——要么组件幂等可复用，要么接受注册后常驻（内存可控时）。
- 事件总线 vs WC 事件：子应用内部交互走组件 CustomEvent；跨子应用通信走共享 store 或自定义总线，避免 DOM 事件跨容器误传（composed 事件可能冒到主应用）。
- 版本治理：主应用锁定共享依赖版本 + 子应用 CI 校验 peerDependencies，防止两个子应用各带一份不同版本运行时。

```javascript
// 主应用：共享 store 单例
window.__ACME_STORE__ = createStore({ user: null, theme: 'light' });
// 子应用 A/B：同一 store 实例（通过全局注册表获取）
import { createStore } from '@acme/signals-core';
const store = window.__ACME_STORE__ ?? createStore({ user: null, theme: 'light' });
window.__ACME_STORE__ ??= store;   // 幂等
// 主题：主应用 :root{--acme-primary}，子应用 WC 影子树 var(--acme-primary) 直接继承
```
