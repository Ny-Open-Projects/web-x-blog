---
title: [FRP-060] 静态提升（hoistStatic）的判定条件是什么？为什么大静态子树提升为 VNODE_CALL、小片段提升为字符串？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-060：静态提升（hoistStatic）的判定条件是什么？为什么大静态子树提升为 VNODE_CALL、小片段提升为字符串？

**答**：
- 判定条件（getConstantType）：节点**不含任何动态绑定**——无插值、无指令、无动态 props/key/ref；组件节点因 `slot` 与 props 的不确定性永远不算静态；表达式必须是纯字面量（含可折叠的字符串拼接）。
- 常量类型分档：0 非静态 / 1 **可提升的字符串**（纯文本节点，直接提到 render 外成为字符串常量，复用时零成本）/ 2 **可缓存的 VNODE_CALL**（整棵纯静态元素子树，提升为常量 vnode，diff 时可直接跳过）。
- 为什么分档：字符串是值不可变、共享绝对安全；vnode 是对象，若被修改（如 v-html 注入、SSR placeholding）会有共享可变状态风险，只有确定安全的纯元素树才提升成 vnode。
- 收益：render 重跑时静态 vnode 直接引用同一个对象，**patch 走 `old === new` 短路**，且不会被收集进 dynamicChildren。

```javascript
// 简化实现，帮助理解静态提升判定与两种提升产物
const ConstantTypes = { NOT_CONSTANT: 0, CAN_STRINGIFY: 1, CAN_HOIST: 2 };

function getConstantType(node) {
  if (node.type === 'TEXT') return ConstantTypes.CAN_STRINGIFY;  // 纯文本可字符串化
  if (node.type !== 'ELEMENT') return ConstantTypes.NOT_CONSTANT;
  if (node.tagType === 'COMPONENT') return ConstantTypes.NOT_CONSTANT; // 组件一律不算
  if (Object.keys(node.dynamicProps || {}).length) return ConstantTypes.NOT_CONSTANT;
  // 所有孩子都静态，自身才是 CAN_HOIST；只要有 CAN_STRINGIFY 孩子则降到该档
  let type = ConstantTypes.CAN_HOIST;
  for (const child of node.children) {
    const ct = getConstantType(child);
    if (ct === ConstantTypes.NOT_CONSTANT) return ConstantTypes.NOT_CONSTANT;
    if (ct < type) type = ct;
  }
  return type;
}

function hoistStatic(ast) {
  ast.hoists = [];
  ast.children.forEach(function walk(node) {
    const ct = getConstantType(node);
    if (ct === ConstantTypes.CAN_STRINGIFY) {
      node.codegenNode = JSON.stringify(node.content);       // 提升为字符串常量
      ast.hoists.push(node);
    } else if (ct === ConstantTypes.CAN_HOIST) {
      node.codegenNode = { isStatic: true, vnode: node };    // 提升为共享 vnode
      ast.hoists.push(node);
    }
    (node.children || []).forEach(walk);
  });
  return ast;
}

const ast = hoistStatic(parse('<div><span>title</span><b>bold</b></div>')); // parse 为编译器前置阶段，此处示意调用
console.log('提升数量:', ast.hoists.length);                       // 2
console.log(getConstantType(parse('<p>{{ msg }}</p>').children[0])); // 0 插值非静态
console.log(getConstantType({ type: 'ELEMENT', tagType: 'COMPONENT' })); // 0 组件非静态
```

## 追问（补充）

**追问**：

1. 静态提升和 Block Tree 是怎么配合的？ → 提升发生在编译期，运行时 patch 只遍历 block 的 dynamicChildren；静态子树连同它的 vnode 都不进 dynamicChildren，于是"跳过 diff"才真正成立，两者缺一不可。
2. 哪些看着像静态的写法其实不能提升？ → 含 v-html、v-text 会改写子节点的元素，带动态 key/ref 的节点，以及插槽内容（由父级决定），都不满足纯静态条件，组件节点更是一律不提升。
3. 提升成共享 vnode 后，如果运行期有人改了它的 el 会怎样？ → 会污染所有复用该常量的实例，因为大家引用同一个对象。这正是只对"确定纯静态元素"才提升的原因，遇到 teleport、v-html 这类需要独立实例的场景要走 cloneVNode。
