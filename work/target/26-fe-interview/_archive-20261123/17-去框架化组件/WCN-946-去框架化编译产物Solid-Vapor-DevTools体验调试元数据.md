---
title: [WCN-946] 去框架化编译产物（Solid / Vue Vapor）的 DevTools 体验怎么补
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-946：去框架化编译产物（Solid / Vue Vapor）的 DevTools 体验怎么补

**答**：
- 结论先行：编译式框架把组件编译成命令式 DOM 操作，传统「组件树面板」失效——要补 DevTools，得靠「编译器注入调试元数据 + 自定义面板」还原组件/信号关系。
- 手段一：编译产物在开发态给每个节点的创建处挂 `__owner` / `__source`（组件名、模板位置），面板据此重建虚拟组件树。
- 手段二：暴露信号依赖图（订阅关系、当前值、触发次数）给可视化面板，定位「为什么这个 effect 又跑了」——这是细粒度框架的独有调试需求。
- 手段三：与浏览器 Elements 面板联动——点选 DOM 节点反查组件与信号；用 `customElements` 的 observedAttributes 日志追踪属性流。
- 追问钩子：面试官问「生产环境要不要保留这些元数据」——答：默认剥离，需要线上排查时通过 swc 插件按白名单注入轻量追踪，避免体积与信息泄露。

```javascript
// 编译器注入调试元数据（开发态）
function createNode(tag, meta) {
  const el = document.createElement(tag);
  if (process.env.NODE_ENV !== 'production') {
    el.__debug = { component: meta.component, tplLine: meta.line, signals: meta.signals };
  }
  return el;
}
const btn = createNode('button', { component: 'BuyBox', line: 12, signals: ['count'] });
// 自定义面板：点选节点后读取 __debug 还原来源
console.log(btn.__debug); // { component:'BuyBox', line:12, signals:['count'] }
```
