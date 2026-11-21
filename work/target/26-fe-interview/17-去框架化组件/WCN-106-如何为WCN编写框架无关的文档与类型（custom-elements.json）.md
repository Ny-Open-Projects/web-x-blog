---
title: [WCN-106] 如何为 WCN 编写框架无关的 API 契约？custom-elements.json 与类型生成怎么做？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-106：如何为 WCN 编写框架无关的 API 契约？custom-elements.json 与类型生成怎么做？

**答**：
- `custom-elements.json`（社区标准 manifest）：声明 tagName、attributes（类型/默认值）、properties、events（detail 结构）、slots、cssParts、cssProperties——一份契约同时服务 IDE 补全、文档站、框架适配层代码生成。
- 类型生成：从 manifest 生成 React 的 JSX.IntrinsicElements 扩展与 Vue 的 GlobalComponents 声明（`.d.ts`），三个宿主的类型一致性由单一源保证。
- 事件契约：detail 的 TS 类型必须显式声明（`CustomEvent<{ value: number }>`），否则宿主只能拿 any。
- 文档站：Storybook + custom-elements manifest 插件可自动渲染 props/事件表格与交互演示；Playwright 截图做视觉回归。
- 版本治理：manifest 进 CI diff——attribute 删除/类型变化视为 breaking，触发版本号与迁移说明。

```json
{
  "filePath": "src/dialog.js",
  "tagName": "x-dialog",
  "attributes": [{ "name": "open", "type": "boolean", "default": false }],
  "events": [{ "name": "dialog-close", "type": "CustomEvent<{action:string}>" }],
  "slots": [{ "name": "footer" }],
  "cssParts": [{ "name": "panel" }],
  "cssProperties": [{ "name": "--x-dialog-width" }]
}
```

```ts
// 生成的 React 类型（示意）
declare module 'react' {
  namespace JSX {
    interface IntrinsicElements {
      'x-dialog': React.HTMLAttributes<HTMLElement> & {
        open?: boolean;
        'onDialogClose'?: (e: CustomEvent<{ action: string }>) => void;
      };
    }
  }
}
```
