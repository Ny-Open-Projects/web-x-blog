---
title: [MFW-562] 元框架与微前端混搭：嵌套 App 的路由协同
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-562：元框架与微前端的嵌套路由协同

**答**:
- 场景：主 App（Next）+ 嵌套子 App（旧 SPA/另一 Next）——三种集成：1) **iframe**（最强隔离 RBL-766——通信 postMessage、路由不同步（history 两个栈））；2) **Module Federation**（共享依赖 RBL-688——运行时拼装，路由各自管理）；3) **网关按路径分流**（/shop → Next、/admin → 旧 SPA——独立部署独立路由——URL 层面切割（最简单可靠））。
- 跨 App 路由协同的痛点：软导航跨 App 边界（Next Link 到旧 SPA 路径 = 硬导航——Link 判断 target 是否本 App）；「面包屑/导航状态跨 App」的同步（postMessage/URL 查询参数）。
- 选型依据：团队/发布节奏隔离度——路径分流（独立部署零耦合）> MF（运行时共享依赖但构建耦合）> iframe（强隔离但体验差）。
- 追问钩子：为什么「网关路径分流」在大多数场景优于 Module Federation？——MF 的耦合面：共享依赖版本协商（RBL-689）+ 构建期声明 + 运行时序（加载顺序竞态）——复杂度换「共享 runtime 省内存」；路径分流 = URL 层切割（每个 App 独立构建部署/独立缓存/独立灰度 RBL-916）——「独立部署的运维价值 > 共享 runtime 的内存收益」在大多数中后台成立；MF 的甜区是「同页面多团队 UI 拼装」（不是跨页面）。

```javascript
// 网关路径分流（最简集成）
// /shop/**  → Next App A (standalone)
// /admin/** → 旧 SPA（静态）
// next.config A: basePath '/shop'（RBL-556）
// 跨 App 软导航判断（Link 降级硬导航）
function isInternal(href) {
  return href.startsWith('/shop') || href.startsWith(basePath);
}
<a href={target} onClick={(e) => {
  if (!isInternal(target)) return;                       // 跨 App：原生硬导航
  e.preventDefault(); router.push(target);               // 本 App：软导航
}}>订单管理</a>
// MF 集成的序（只在同页拼装时用）
const remote = await loadRemote('admin/Header');         // 运行时加载子 App 组件
// 版本协商：shared react singleton requiredVersion（RBL-689）
```
