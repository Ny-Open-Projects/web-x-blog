---
title: [V3-519] 笔试：手写 Teleport 简版
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 编译器]
type: 笔试题
---

## V3-519：笔试：手写 Teleport 简版

**答**：实现 `MyTeleport`：① props: { to: string|Element, disabled?: boolean }；② mount：children 渲染后 DOM 移入目标容器（querySelector 支持）；③ disabled=true 原地渲染（不移动）；④ unmount 时从目标容器移除；⑤ target 与逻辑树分离——provide/inject 仍从原组件链取（实现上 Teleport 子树 vnode 的 parent 指针保持不变）。写出实现。

```javascript
import { h, getCurrentInstance } from 'vue';

const MyTeleport = {
  name: 'MyTeleport',
  props: { to: [String, Element], disabled: Boolean },
  setup(props, { slots }) {
    const inst = getCurrentInstance();
    return () => {
      const target = typeof props.to === 'string'
        ? document.querySelector(props.to) : props.to;
      const children = slots.default();
      // 标记: patch 层据此决定挂载点
      inst.vnode.tt = { target, disabled: props.disabled };
      return children;
    };
  },
};
// patch 层伪代码(挂载分支):
// if (vnode.tt && !vnode.tt.disabled && vnode.tt.target)
//   mountChildren(vnode, vnode.tt.target)   // 直接挂到目标容器
// unmount 分支:
// if (vnode.tt?.target) removeChildrenFrom(vnode.tt.target, vnode)
```

**评分点**：
- DOM 挂载点切换在 patch 层（mount 时直接挂目标容器），组件树 parent 不变
- disabled 原地渲染的分支
- 目标选择器解析与容错（找不到 target 时的告警）
- unmount 从目标容器清理
