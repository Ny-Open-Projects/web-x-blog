---
title: [WCN-685] Design-to-Code（设计稿转代码）在现实项目中能落地到什么程度？边界在哪？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-685：Design-to-Code（设计稿转代码）在现实项目中能落地到什么程度？边界在哪？

**答**：
- 结论：能较好生成「结构 + 样式骨架 + token 引用」，但难生成业务逻辑与语义化交互；定位是「提效工具」而非「替代开发」。
- 前提：设计规范严格（图层命名/自动布局/组件实例化）；输出与代码库 token/组件映射匹配；生成代码需人工 review。
- 追问钩子：为什么强规范是前提？因为设计稿若随意图层，机器无法推断语义——考察对「AI/自动化依赖结构化输入」的认知。

```javascript
// 设计稿图层 → 代码映射（示意）
const figmaNode = {
  type: 'FRAME', name: 'Button/Primary', fills: [{ color: '#165DFF' }],
  layoutMode: 'HORIZONTAL', children: [{ type: 'TEXT', characters: '提交' }],
};
function nodeToCode(node) {
  const tag = node.name.split('/')[0].toLowerCase();
  const token = mapColorToToken(node.fills?.[0]?.color);
  return `<ds-${tag} style="--bg:var(${token})">${
    node.children?.map(c => c.characters || '').join('') || ''}</ds-${tag}>`;
}
function mapColorToToken(hex) {
  return hex === '#165DFF' ? '--ds-color-primary' : '--ds-color-custom';
}
console.log(nodeToCode(figmaNode));
```
