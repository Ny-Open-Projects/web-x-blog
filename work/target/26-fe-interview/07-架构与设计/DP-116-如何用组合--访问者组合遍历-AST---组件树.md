---
title: [DP-116] 如何用"组合 + 访问者"组合遍历 AST / 组件树？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-116：如何用"组合 + 访问者"组合遍历 AST / 组件树？（高频）
**答**：
- 组合模式建树：节点统一暴露 `children` 与 `accept(visitor)`，叶子与容器同构（DP-036）；访问者把"对节点的操作"从树结构中剥离，新增遍历目的（收集、校验、转换）不改节点类。
- 与 babel 对应（DP-065）：enter/leave 两阶段访问，访问者可返回替换节点实现改写。
- 前端实例：组件树抽取所有表单字段、埋点扫描器、主题变量收集器。

```javascript
// 组合模式：统一节点
class VNode {
  constructor(type, props = {}, children = []) { Object.assign(this, { type, props, children }); }
  accept(visitor) {
    visitor.enter?.(this);
    this.children.forEach((c) => c.accept(visitor));        // 容器递归，叶子 children 为空，结构同构
    visitor.leave?.(this);
  }
}
const tree = new VNode('Form', {}, [
  new VNode('Input', { name: 'user', rules: 'required' }),
  new VNode('Group', {}, [ new VNode('Select', { name: 'city' }), new VNode('Input', { name: 'phone' }) ]),
]);
// 访问者1：收集所有带校验规则的字段
const collectVisitor = {
  fields: [], enter(n) { if (n.props.rules) this.fields.push(n.props.name); },
};
// 访问者2：扫描埋点埋没埋（同一棵树，另一个操作）
const trackVisitor = { miss: [], enter(n) { if (n.type === 'Input' && !n.props.trackId) this.miss.push(n.props.name); } };
tree.accept(collectVisitor);
tree.accept(trackVisitor);
console.log(collectVisitor.fields);   // [ 'user', 'phone' ]
console.log(trackVisitor.miss);       // [ 'user', 'phone' ] —— 新增遍历目的零改树
```

---

## 十四、React 业务模式深化
