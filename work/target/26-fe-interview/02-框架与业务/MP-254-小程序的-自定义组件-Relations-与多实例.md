---
title: [MP-254] 自定义组件 Relations 与多实例生命周期坑？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-254：Relations 与多实例坑？
**答**：
- relations：组件树关联（父子的 linked/unlinked 回调），用于 form/picker 组合类组件（子注册到父）。
- 多实例坑：custom-tab-bar/页面级组件每页一份——全局单例假设失效；static/模块级变量被多实例共享——状态要用实例字段。
- 生命周期：attached（实例创建）、ready（渲染完成）、detached（卸载）；页面生命周期要用 pageLifetimes（组件感知页面 show/hide）。
- 事件系统：triggerEvent 向上、selectComponent/selectOwnerComponent 向下/上查找——过度使用破坏封装，白名单场景用。
- 实践：组合类组件用 relations 注册表 + detached 注销，防泄漏。
