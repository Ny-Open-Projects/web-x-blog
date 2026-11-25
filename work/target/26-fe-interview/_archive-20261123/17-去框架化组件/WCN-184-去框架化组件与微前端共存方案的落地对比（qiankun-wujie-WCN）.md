---
title: [WCN-184] qiankun / wujie / WCN 三种"复用与隔离"方案的落地对比怎么写？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-184：qiankun / wujie / WCN 三种方案的落地对比

**答**：
- qiankun：JS 沙箱（Proxy 快照）+ 样式隔离（scoped/strictStyleIsolation），子应用整页级；成本 = 生命周期改造与公共依赖协调；适合"遗留多技术栈整站聚合"。
- wujie：iframe + proxy 组合（iframe 渲染、主应用沙箱），保活与通信更强；成本 = iframe 内存与通信复杂度；适合需要保活、强隔离的中后台。
- WCN：组件级复用、原生隔离、无容器框架依赖；不适合整页聚合（路由/全局状态接管缺失）。
- 组合实践：主平台用 qiankun/wujie 聚合子应用；子应用对外以 WC 导出可嵌部件（WCN-054），跨子应用/主应用复用走 WCN——分层使用而非二选一。
- 决策输入：聚合粒度（页 vs 组件）、隔离强度（信任边界）、保活需求、团队容器运维能力。

```text
对比速查
              qiankun    wujie      WCN
粒度          整页        整页        组件
JS 隔离       Proxy沙箱   iframe+proxy 无(共享)
样式隔离      可选        强(iframe)  Shadow DOM
保活          弱          强          N/A
通信          props/bus   props/bus   事件/共享store
典型场景      遗留聚合    中后台平台   设计系统/SDK
```
