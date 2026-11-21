---
title: [WCN-282] Vue Vapor 模式的编译策略与运行时（无 VDOM）实现？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-282：Vue Vapor 模式的编译策略与运行时（无 VDOM）实现？
**答**：
- 编译期：模板静态分析 → 静态节点提升 + 动态绑定标记（block 结构），生成直接 DOM 操作函数。
- 运行时：无 VDOM 无 diff——更新是编译期生成的定向函数（bk/bind 系列 helper）。
- 兼容性：Vapor 与现有 VDOM 模式可同页共存（渐进迁移）。
- 代价：编译产物体积增大（每组件携带定向代码）换取运行时删除 diff——总体常更小。

```javascript
// Vapor 产物形态
const t0 = _template('<div><span> </span></div>');
export default function Comp(props) {
  const n0 = t0(), n1 = _child(n0);
  _setProp(n1, 'id', () => props.id);        // 定向绑定
  _createIf(_computed(() => props.show), () => t1());   // if 也是编译期结构化
  return n0;
}
r
```
