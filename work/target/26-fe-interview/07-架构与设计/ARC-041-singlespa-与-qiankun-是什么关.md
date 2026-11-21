---
title: [ARC-041] single-spa 与 qiankun 是什么关系？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-041：single-spa 与 qiankun 是什么关系？
**答**：
- single-spa 是微前端"内核"：只负责生命周期编排（registerApplication、load、mount/unmount 状态机）与路由激活规则，不解决沙箱、样式隔离、HTML 加载。
- qiankun 基于 single-spa 封装：补齐了 HTML Entry（import-html-entry 解析子应用 HTML）、JS 沙箱、样式隔离、预加载、全局错误兜底，是"开箱即用层"。
- 类比：single-spa 是 React 未封装的 scheduler+reconciler，qiankun 是 umd 之上的完整框架。

```typescript
// single-spa 原生注册：一切自己来
import { registerApplication, start } from 'single-spa';
registerApplication({
  name: 'app-trade',
  app: () => System.import('@corp/app-trade'),      // 加载方式自己解决
  activeWhen: ['/trade'],                            // 路由激活规则
  customProps: { authToken: 'xxx' },
});
start();

// qiankun：在 single-spa 之上补齐 HTML Entry + 沙箱 + 隔离
import { registerMicroApps, start } from 'qiankun';
registerMicroApps([
  {
    name: 'app-trade',
    entry: '//trade.corp.com',       // HTML Entry：qiankun 负责解析 html 并执行其中 JS
    container: '#subapp',
    activeRule: '/trade',
    props: { authToken: 'xxx' },
  },
]);
start({ sandbox: { experimentalStyleIsolation: true }, prefetch: 'all' });
```
