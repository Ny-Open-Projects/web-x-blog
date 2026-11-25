---
title: [XP-211] Flutter 渲染管线：Widget-Element-RenderObject 三棵树
date: 2026-11-21
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-211：Flutter 渲染管线：Widget-Element-RenderObject 三棵树

**答**：
- Flutter 三棵树：Widget（声明式配置，不可变）→ Element（生命周期/复用）→ RenderObject（布局/绘制）。
- 更新流程：setState → Widget 重建 → Element diff（canUpdate：同 type+key 复用）→ RenderObject 更新属性（不重建）。
- 性能关键：Element 复用减少 RenderObject 重建；const Widget（编译期常量，跳过重建）。

```javascript
const flutterTrees = {
  widget: '声明式配置（不可变，每次 build 重建）',
  element: '生命周期持有者（diff 复用：runtimeType + key 相同则复用）',
  renderObject: '布局/绘制实体（属性更新，不重建）',
  flow: 'setState → build() 新 Widget → Element diff → RenderObject.updateRenderObject',
  perf: [
    'const Widget：编译期常量——build 重建跳过（不产生新实例）',
    'Element 复用：同 type+key → 不重建 RenderObject',
    '避免整棵子树 rebuild：拆分 widget / 用 builder 惰性构建',
  ],
};
```
