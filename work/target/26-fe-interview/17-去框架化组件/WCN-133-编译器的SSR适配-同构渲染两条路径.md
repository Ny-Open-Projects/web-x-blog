---
title: [WCN-133] 编译器框架的 SSR 适配：同一条组件代码如何同时输出字符串与 DOM 操作？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-133：编译器框架的 SSR 适配：同一条组件代码如何同时输出字符串与 DOM 操作？

**答**：
- 双目标编译：同一组件编译两份产物——SSR 版（组件函数返回字符串拼接，插值即模板插值）与客户端版（返回 DOM 操作 + effect）；由构建时条件（环境变量/打包入口）选择。
- Solid 方案：`solid-js/web` 双实现——server 模块把 `template/insert/effect` 实现为字符串拼接与跳过，client 模块是真实 DOM 操作；应用代码零改动。
- 水合接口：SSR 输出带注释节点标记动态位置（`<!> template`），客户端水合时用 `dehydration` 定位既有节点、重新绑定 effect（不重新创建 DOM）。
- Vue Vapor/Svelte：SSR 版走渲染为字符串路径（vdom 模式复用现有 SSR runtime），客户端版本走细粒度 DOM。
- 共同难点：事件与 effect 不应在服务端执行；资源（样式提取）、流式输出与错误边界的双实现成本。

```javascript
// solid 双实现示意（同一调用面）
// server.js
export const template = (html) => () => html;          // 返回字符串
export const insert = (parent, get) => (parent += get() ?? '');
export const effect = () => {};                         // 服务端跳过副作用
// client.js
export const template = (html) => range(document.createRange().createContextualFragment(html));
export const insert = (parent, get) => insertEl(parent, get);
export const effect = (fn) => renderEffect(fn);
```
