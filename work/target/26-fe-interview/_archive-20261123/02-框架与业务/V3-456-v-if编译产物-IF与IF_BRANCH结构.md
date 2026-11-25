---
title: [V3-456] v-if 编译产物：IF 与 IF_BRANCH 结构化节点
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 面试题, 编译器]
type: 面试题
---

## V3-456：v-if 编译产物：IF 与 IF_BRANCH 结构化节点

**答**：
- 结构转换：v-if 元素被 transform 成 `IF` 节点，其 branches 数组收集各分支（if/else-if/else 各一个 branch）——branch 内含 condition 与真实节点
- 运行时代码：`_conditional ? branch1 : branch2` 三元表达式（codegen 层生成），runtime 里 createIf 用 _resolveDynamicComponent 风格切换——不是 v-show 那种 display 切换
- 与 v-for 同元素时的优先级：v-if 优先于 v-for（编译器直接报错提示，Vue3 要求分开写）——因为 FOR 在外层会丢失 if 的分支语义
- branch 内的 key：v-if/v-else 分支默认无 key 也会被 patch 时当不同节点处理（不同 branch 意味重建）——「同 tag 两个 branch 状态不保留」的原因
- 深水点：IF 节点的 transform 在 enter 阶段抓取后续兄弟节点（else-if 链），用 ctx.removeNode 摘走——这是「transform 能跨节点操作」的经典案例

```javascript
// 编译产物示意
show
  ? _createElementVNode('div', { key: 0 }, 'A')
  : _createElementVNode('span', { key: 1 }, 'B')
// runtime: 分支切换 = 卸载旧分支 + 挂载新分支(状态不保留)
```
