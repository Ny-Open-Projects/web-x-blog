---
title: [WCN-654] 编译器如何区分动态/静态节点？patchFlag 的作用是什么？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-654：编译器如何区分动态/静态节点？patchFlag 的作用是什么？

**答**：
- 结论：编译期给节点打 patchFlag 标记「哪些部分是动态的」（如 TEXT/CLASS/PROPS），运行时 diff 只检查标记部分，跳过静态子树。
- 机制：纯静态子树提升为常量并复用；带 patchFlag 的节点只比较对应类型；动态节点用 block 树按稳定顺序更新。
- 追问钩子：patchFlag 失效的场景？v-if 切换导致节点顺序变化时 block 不稳定，需回退全量 diff——考察对优化边界的理解。

```javascript
// 编译器为节点打标记（Vue 3 风格）
const CREATE_ELEMENT = {
  text:  1, // CLASS
  cls:   2, // STYLE
  props: 4, // PROPS
};
function patchElement(n1, n2) {
  if (n2.patchFlag & CREATE_ELEMENT.text) {
    if (n1.children !== n2.children) n1.el.textContent = n2.children;
  }
  if (n2.patchFlag & CREATE_ELEMENT.cls) {
    n1.el.className = n2.className;
  }
  // 未标记的部分完全跳过 → 静态子树零 diff 成本
}
const node = { patchFlag: CREATE_ELEMENT.text, children: '新文本' };
```
