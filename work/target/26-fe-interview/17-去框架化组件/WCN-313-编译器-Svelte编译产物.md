---
title: [WCN-313] Svelte 5 的编译产物与 Svelte 4 的差异（运行时信号引入）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-313：Svelte 5 的编译产物与 Svelte 4 的差异（运行时信号引入）？
**答**：
- S4：编译期完全定向更新（无运行时响应式）——跨组件动态场景受限。
- S5：运行时信号（$state 节点）+ 编译期优化（静态提升/表达式拆分）。
- 产物对比：S5 组件产物含信号节点创建代码——包体积略增，能力提升。
- 选择：简单静态页 S4 思路仍省；复杂交互 S5 更强。

```javascript
// Svelte 5 产物示意
let count = $.signal(0);
const double = $.derived(() => $.get(count) * 2);
// 模板节点 + $.template + 定向 effect（编译期优化保留）
r
```
