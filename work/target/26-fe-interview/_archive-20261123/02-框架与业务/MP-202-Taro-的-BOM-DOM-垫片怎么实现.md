---
title: [MP-202] Taro 的 BOM/DOM 垫片怎么实现（让 React 以为在浏览器）？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-202：Taro 的 BOM/DOM 垫片怎么实现？
**答**：
- 小程序逻辑层没有 DOM/BOM——Taro 实现了 document/window/Element/NodeTree 的模拟对象（TaroDocument），React reconciler 以它为 host。
- 实现：基于 @tarojs/runtime 的 TaroNode 树（每个节点对应小程序组件实例），appendChild/setAttribute 操作真实映射。
- 桥接：虚拟树变更 → diff → 生成 setData 增量数据 → 渲染层更新。
- 事件：渲染层事件冒泡回逻辑层，找到 TaroNode 挂的 handler 模拟合成事件。
- 兼容技巧：伪造 location/navigator/localStorage 到小程序 API（wx.getStorageInfo 等）。
