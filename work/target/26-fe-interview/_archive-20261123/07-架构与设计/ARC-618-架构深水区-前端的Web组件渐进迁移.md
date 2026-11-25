---
title: [ARC-618] 老系统向 Web Components 的渐进迁移架构如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-618：Web Components 渐进迁移
**答**:
- 适用场景：技术栈异构共存（jQuery 老页 + Vue 新页 + React 工具页——需要真正框架无关的组件层，ARC-17 去框架化组件专题的技术选型）。
- 迁移策略：新通用组件用 WC 实现（一次编写多框架消费——ARC-WCN 桥接：Vue/React 各自 wrapper）、老组件按"被多框架需要"的优先级重写为 WC、框架特有组件保持原框架（不为 WC 而 WC——异构共存的交集部分才值得）。
- 集成架构：WC 注册中心（自定义元素注册统一管理——避免重名冲突）、样式基座（Design Token CSS 变量全局注入——WC ::part 暴露主题化 ARC-561）、事件协议（WC 自定义事件命名规范 + 框架侧监听封装）。
- 渐进路径：jQuery 老页直接用 WC（无框架包袱——最小改动引入新能力）、新旧页面共享同一组件（UI 一致性达标——跨技术栈视觉统一）。
- 治理：WC 组件清单与框架 wrapper 版本对齐、双实现期管理（老组件与 WC 并存期明确淘汰日期——ARC-425 迁移纪律）。
```javascript
// 跨框架 WC 使用
customElements.define('x-date-range', DateRange);                // 注册中心统一
// Vue: <x-date-range :value="v" @change="...">  React: <x-date-range value={v} onChange={...}>
// 桥接：React19 已支持自定义元素 props 直传（官方）——wrapper 只处理事件与类型
```
