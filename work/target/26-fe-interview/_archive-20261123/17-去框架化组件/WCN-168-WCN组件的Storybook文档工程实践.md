---
title: [WCN-168] WCN 组件的文档工程实践：Storybook/Docs 站如何覆盖 WC 特有的文档需求？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-168：WCN 组件的文档工程实践：Storybook/Docs 站如何覆盖 WC 特有需求？

**答**：
- 文档维度差异：除 props 外，WC 要文档化 attributes vs properties 的区分、events（detail 结构）、slots（含具名）、cssParts、cssProperties——这些恰是 custom-elements.json 的字段，用 custom-elements-manifest 插件自动生成参数表。
- 多宿主示例页：每个组件给 React/Vue/native 三份使用代码（tabs 切换），示例可一键复制；宿主代码与 adapters 版本绑定测试（示例失效即 CI 报错）。
- 交互文档：键盘行为表、状态伪类（:--loading）说明、生命周期注意事项（如 connectedCallback 里不要 attachShadow 两次）。
- Playground：在线编辑 attribute/slot 实时预览（iframe 隔离 + importmap 加载组件）。
- 发布联动：docs 站版本化（每组件版本一页），deprecate 标记醒目展示迁移指引。

```js
// .storybook/preview.js：WC 组件注册
import '../dist/button/button.define.js';
import '../dist/button/custom-elements.json';   // manifest 驱动参数表

// 文档页 stories 示例
export const Basic = {
  render: () => `<acme-button tone="primary">主按钮</acme-button>`,
};
export const WithSlot = {
  parameters: { docs: { description: { component:
    '键盘：Enter/Space 触发。事件 acme-click detail:{source}. cssPart: root.' } } },
  render: () => `<acme-button><acme-icon slot="icon"></acme-icon>带图标</acme-button>`,
};
```
