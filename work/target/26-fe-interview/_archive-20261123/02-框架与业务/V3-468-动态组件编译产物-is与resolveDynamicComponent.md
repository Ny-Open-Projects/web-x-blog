---
title: [V3-468] 动态组件：compilation is 与 resolveDynamicComponent
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-468：动态组件：compilation is 与 resolveDynamicComponent

**答**：
- `<component :is="x">` 编译：is 为动态绑定 → `_resolveDynamicComponent(x)`——运行时先查注册组件再当原生标签；is 为静态字符串则编译期直接解析
- 三种 is 值形态：字符串（注册组件名/HTML 标签）、组件对象（script setup 直接 import 的变量）、组件定义（defineAsyncComponent 包装）——运行时 resolve 分支不同
- 与 keep-alive 组合：`<KeepAlive><component :is="x"/></KeepAlive>` 缓存键按 type（组件对象）——字符串切换时 resolve 出的是同一对象可复用缓存；匿名组件对象每次新建则缓存失效
- 原生元素陷阱：is 传「未注册组件名」会渲染为原生标签（div/is 大小写敏感）——`<component is="myWidget">` 找不到组件渲染成未知元素，dev 有告警
- Vue3 移除了「普通元素上的 is」（Vue2 的 hack）→ 改用 vue: 前缀（is="vue:div" 在原生元素上渲染 Vue 组件）——DOM 模板约束下的兼容方案

```javascript
// <component :is="view" /> 产物
_createBlock(_resolveDynamicComponent($setup.view))
// resolveDynamicComponent: registry.get(name) ?? name(当原生标签)
```
