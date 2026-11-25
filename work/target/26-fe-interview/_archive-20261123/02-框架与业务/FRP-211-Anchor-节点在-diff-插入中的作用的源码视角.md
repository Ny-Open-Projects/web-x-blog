---
title: [FRP-211] 锚点（anchor）节点在 diff 插入中的作用（源码视角）？
date: 2026-11-19
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-211：锚点（anchor）在 diff 插入中的作用？
**答**：
- 插入需要知道「插到谁前面」：insertBefore(el, anchor)，anchor 是目标位置的参考节点。
- 场景一：头部插入——anchor = 旧首节点；尾部插入——anchor = null（appendChild 语义由框架包装）。
- 场景二：Fragment/多根组件插入——anchor 指向 fragment 末尾后的节点，否则插错位置。
- 场景三：Teleport/卸载中集合——anchor 配合占位注释节点（React 用空文本节点标记 fragment 边界）。
- Vue3 源码：patch 的 container 参数分离（mount 时 container 是 fragment 容器），anchor 贯穿插入/卸载 API。
