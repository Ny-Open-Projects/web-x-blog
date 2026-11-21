---
title: [MFW-253] App Router 与微前端组合的约束
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-253：App Router × 微前端

**答**:
- 根本约束：App Router 的路由/缓存/水合是整页单实例语义——多 App Router 子应用同页嵌套（路由器冲突/双 React 树水合）不可行
- 可行组合：①一个 Next App Router 壳 + 非 React 子应用 islands（Web Components/iframe）②MF 加载远程 RSC 不可行（RSC payload 引用宿主编译器产物——跨构建边界断裂），远程只能是纯 client chunk ③路由级 MF（不同路径整页切换给不同应用——不嵌套）
- 推荐：微前端需求下 Next 只做壳（布局/鉴权/公共 layout），业务域独立部署为客户端 bundle 由壳的客户端组件动态挂载
- 判定：真需要跨团队整页自治 → 路由级分离（各应用独立 Next 实例 + 网关分发）——比硬嵌健康得多

```text
可行度表：
同页嵌套多 App Router   ✗（路由器/水合冲突）
MF 加载远程 RSC        ✗（payload 跨构建断裂）
MF 加载纯 client 岛    ✓
路由级多实例 + 网关     ✓✓（推荐）
```
