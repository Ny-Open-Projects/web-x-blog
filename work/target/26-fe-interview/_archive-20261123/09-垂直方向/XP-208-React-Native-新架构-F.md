---
title: [XP-208] React Native 新架构 Fabric：渲染器重构
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-208：React Native 新架构 Fabric：渲染器重构

**答**：
- Fabric：RN 新渲染器——同步可中断渲染（类 React 18 并发）、C++ 共享 Core（跨平台一致）、优先级渲染。
- 对比旧 Paper：Paper 异步批量（桥 JSON）、布局单位不一致（iOS/Android 各自实现）——Fabric 统一 C++。
- 前端影响：组件行为更接近 Web（同步布局读取）、新旧架构混合模式（interop layer）。

```javascript
const fabricVsPaper = {
  paper: { bridge: '异步 JSON 批量（桥）', layout: '平台各自实现（iOS Yoga / Android 自己）',
    sync: '异步——无法同步读布局' },
  fabric: { renderer: 'C++ 共享（Shadow Tree）',
    sync: '同步可中断渲染（React 18 并发兼容）',
    layout: '统一 Yoga（C++）——跨平台一致' },
  jsImpact: 'getBoundingClientRect 类操作可同步读（Fabric）——Paper 不行',
  interop: '新旧组件混跑（interop layer）——渐进迁移路径',
};
```
