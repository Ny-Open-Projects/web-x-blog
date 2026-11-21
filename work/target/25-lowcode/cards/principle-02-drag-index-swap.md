---
title: 拖拽排序的本质：数组索引交换
date: 2026-11-17
categories: [课程, 低代码]
tags: [25-lowcode, 原理, dnd-kit, MobX]
---

## 拖拽排序的本质：数组索引交换

为什么 dnd-kit 拖几个像素就能完成组件排序？因为**排序状态被单独建模为一个 ID 数组**（sortableComponentConfig），画布渲染顺序完全由数组顺序决定。拖拽只是改数组里的位置，不触碰组件配置字典。

实现模型：
1. `DndContext + SortableContext`（传组件 ID 数组 + verticalListSortingStrategy）；
2. 每项 `useSortable` 解构 attributes/listeners/setNodeRef/transform/transition；
3. `useSensors` 的 `distance: 2` 激活约束是区分「点击」与「拖拽」的阈值，`closestCenter` 中心点碰撞检测；
4. transform 的 Y 轴 replace 为空避免样式跳变；
5. `onDragEnd` 取 active/over（over 为 null 直接 return），MobX action 里 `arrayMove(oldIndex, newIndex)`。

**本项目实例**：上移/下移（键盘操作）与拖拽共用同一个 arrayMove——首尾边界提示也一致。持久化时这个数组存进 page.components 字段。

推论：把视图操作翻译成 store 数据的增删改查，是整个编辑器交互的心法，拖拽只是其中一个翻译器。

出处「课程25 · 18-4、18-5」
