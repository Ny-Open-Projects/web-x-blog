---
title: [V3-217] Vapor 组件如何做到完全省掉虚拟 DOM？关键机制是什么？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-217：Vapor 组件如何做到完全省掉虚拟 DOM？关键机制是什么？
**答**：
- 关键机制 1：编译期**静态分析模板**，把每个动态点（文本/属性/事件/结构）定位到具体 DOM 节点与操作。
- 关键机制 2：动态点包装成细粒度 effect（依托 3.5 新响应式），依赖变化只执行对应 DOM 写操作，无需全局重渲染。
- 关键机制 3：Block/Fragment 结构替代 vnode 树——编译器已知组件静态结构，运行时只需记录"动态节点数组"。
- 关键机制 4：事件用 `delegateEvents` 委托，避免每个节点绑定 listener 的开销。
- 前提条件：模板可静态分析。JSX/手写渲染函数无法享受 Vapor，这是模板作为"编译目标"的价值回归。

```javascript
// v-if="show" 的 Vapor 编译（示意）
// <p v-if="show">{{ msg }}</p><p v-else>off</p>
import { template, createIf, setText } from 'vue/vapor';
function setup() {
  const show = ref(true), msg = ref('hi');
  const n2 = template('<p></p>'), n3 = template('<p>off</p>');
  const branch = createIf(() => show.value, () => {
    setText(n2(), () => msg.value);   // 进入分支时才创建 + 建立订阅
    return n2;
  }, () => n3());
  return branch; // show 切换时直接卸载/挂载分支 DOM，无 diff 参与
}
```
