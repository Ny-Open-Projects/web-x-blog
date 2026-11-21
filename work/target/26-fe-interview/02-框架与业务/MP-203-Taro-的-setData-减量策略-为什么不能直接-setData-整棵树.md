---
title: [MP-203] Taro 的 setData 减量策略：为什么不能整树直接 setData？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-203：Taro 的 setData 减量策略？
**答**：
- 整树 setData 的问题：序列化整棵虚拟树 → 数据量大（几 MB）→ 跨线程序列化/传输 → 掉帧。
- Taro 的减量：diff 只取变化路径（如 `root.children[2].text`），按路径 patch 传输；数据按模板预设结构裁剪（模板未引用的字段不传）。
- 辅助手段：更新队列合并（同一 tick 多次 setState 合一）、大于阈值转「整树替换」（极端 diff 反而便宜）、自定义组件边界分片。
- 渲染层模板设计：递归模板 + 简单数组结构，让 setData payload 最小化。
- 度量：setData 数据量与调用次数是 Taro 性能的核心指标。
