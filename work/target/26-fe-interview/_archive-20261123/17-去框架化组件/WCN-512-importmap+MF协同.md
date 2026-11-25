---
title: [WCN-512] 微前端「运行时共享依赖」：importmap、Module Federation 与 WCN 三者如何协同？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-512：微前端「运行时共享依赖」：importmap、Module Federation 与 WCN 三者如何协同？

**答**：
- 结论：importmap 管「裸模块名到 URL 的解析」，MF 管「跨应用模块共享与版本协商」，WCN 作为共享 UI 资产挂在二者之上。
- 把 @ds/core 写进 importmap 指向单一 URL，保证所有应用解析到同一份；MF 暴露/消费该模块避免重复打包。
- WCN 元素通过 core 提供 defineOnce，天然单例；宿主只声明版本，不打包实现。
- 追问：三者都能解决共享，为什么还要叠加？（答：各管一层，单靠 importmap 无版本协商，单靠 MF 无裸名解析）

```javascript
// index.html
// <script type="importmap">{"imports":{"@ds/core":"https://host/ds/v3/core.js"}}</script>
// MF 配置
const mfConfig = {
  name: 'shell',
  remotes: { ds: 'ds@https://host/ds/remoteEntry.js' },
  shared: { '@ds/core': { singleton: true, requiredVersion: '^3.0.0' } },
};
// 业务代码
import { defineOnce } from '@ds/core';
defineOnce('ds-btn', RemoteDsButton, '3.1.0');
```
