---
title: [WCN-238] 微前端架构下 WC 作为「跨应用组件协议」的实践要点？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-238：微前端架构下 WC 作为「跨应用组件协议」的实践要点？
**答**：
- 主应用注册核心元素，子应用消费（统一版本，避免多版本冲突）——版本治理集中化。
- 子应用自有元素用前缀命名空间，注册前查重（customElements.get）。
- 跨应用数据传递用元素 property 传「共享 store 句柄」（与框架无关）。
- 样式隔离：元素 shadow 自带隔离，比微前端 CSS 方案（shadow/scoped）更彻底。

```javascript
// 主应用统一注册
import '@ds/elements';   // define 全部核心元素
// 子应用消费（等注册完成再渲染依赖区）
await customElements.whenDefined('goods-card');
renderSubApp();
r
```
