---
title: [WCN-655] 笔试：实现编译器的 patchFlag 标记生成器（根据节点动态属性算位掩码）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-655：笔试：实现编译器的 patchFlag 标记生成器（根据节点动态属性算位掩码）

**答**：
- 需求：给定节点描述 { tag, dynamicAttrs:[], hasText, hasChildren }，实现 markPatchFlag(node) 返回位掩码：CLASS=1,STYLE=2,PROPS=4,TEXT=8,CHILDREN=16。
- 思路：按属性名归类（class→CLASS, style→STYLE, 其他→PROPS），有动态文本→TEXT，有动态子节点→CHILDREN；按位或合并。
- 边界：未知属性归 PROPS；空节点返回 0；重复属性不重复置位。

```javascript
const FLAG = { CLASS: 1, STYLE: 2, PROPS: 4, TEXT: 8, CHILDREN: 16 };
function markPatchFlag(node) {
  let flag = 0;
  for (const attr of node.dynamicAttrs || []) {
    if (attr === 'class') flag |= FLAG.CLASS;
    else if (attr === 'style') flag |= FLAG.STYLE;
    else flag |= FLAG.PROPS;
  }
  if (node.hasText) flag |= FLAG.TEXT;
  if (node.hasChildren) flag |= FLAG.CHILDREN;
  return flag;
}
function decode(flag) {
  return Object.entries(FLAG).filter(([, v]) => flag & v).map(([k]) => k);
}
console.log(markPatchFlag({
  tag: 'div', dynamicAttrs: ['class', 'title'], hasText: true,
})); // 1 | 4 | 8 = 13
console.log(decode(13)); // ['CLASS', 'PROPS', 'TEXT']
```

**评分点**：
- 位掩码按位或合并正确（不相互覆盖）。
- 属性归类准确（class/style/其他）。
- hasText/hasChildren 对应 TEXT/CHILDREN 位。
- 空节点返回 0，decode 能反向解析便于调试。
