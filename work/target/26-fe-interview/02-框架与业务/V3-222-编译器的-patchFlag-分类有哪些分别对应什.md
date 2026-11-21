---
title: [V3-222] 编译器的 patchFlag 分类有哪些？分别对应什么靶向更新路径？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-222：编译器的 patchFlag 分类有哪些？分别对应什么靶向更新路径？
**答**：
- TEXT=1：动态文本 → patch 只走 `textContent`。
- CLASS=2 / STYLE=4：动态 class/style → 只 diff className/style 属性。
- PROPS=8：动态普通属性 → 按编译时记录的 `dynamicProps` 数组逐项对比，未列出的属性根本不看。
- FULL_PROPS=16：key 变化或整 props 动态（如 v-bind 对象）→ 全量 props diff。
- HYDRATE/STABLE/NEED_PATCH 等辅助位与复合位（如 `9 = TEXT|PROPS`）按位叠加。
- 价值：diff 从"枚举所有属性"变成"按位跳转"，配合 block tree 动态节点只含动态内容，更新成本与模板复杂度解耦。

```javascript
// 编译产物示例
createVNode("div", {
  class: cls,            // 动态
  id: "static-id",       // 静态，编译期直接写死
  title: tip,            // 动态
}, text, 10 /* CLASS(2) | PROPS(8) */, ["class", "title"]);
// 运行时 patch：flag=10 → 只比 class 与 title，id 等静态属性跳过
function patchElement(n1, n2, dynamicProps) {
  for (const key of dynamicProps) {
    if (n1.props[key] !== n2.props[key]) hostPatchProp(el, key, n2.props[key]);
  }
  if (n2.patchFlag & 1) hostSetElementText(el, n2.children);
}
```
