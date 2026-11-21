---
title: [ARC-320] 组件库的文档与 Playground 如何建设？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-320：组件库的文档与 Playground 如何建设？
**答**：
- 文档三要素：API 表（从 TS 类型自动生成，保证与代码同步）、可交互 demo（Storybook stories 直接嵌入）、最佳实践指南（何时用哪个组件/反模式示例）。文档腐烂的根因是"手写 API 表"——必须自动生成。
- Playground：在线编辑 demo 代码实时预览（sandpack/iframe），支持"复制代码/导出到本地"；问题复现沙箱链接（issue 模板强制附 playground 链接，降低维护者排查成本）。
- 搜索与导航：组件按场景分类（而非字母序）+ 全文搜索；版本切换（历史版本文档保留，用户按所用版本查阅）。
- 文档 CI：API 变更自动更新文档站；demo 编译失败卡发布；文档覆盖检查（每个 export 必须有 story + 文档页）。

```typescript
// API 表自动生成（typedoc JSON → 表格）
const apiJson = typedocToJson('ButtonProps');
function renderApiTable(props) {
  return props.map(p => ({
    prop: p.name, type: p.type, default: p.comment?.default ?? '-',
    required: p.flags.isRequired, desc: p.comment?.summary,
  }));   // → markdown 表格，与源码同源
}
// story 嵌入：<StorybookEmbed id="button--primary" />
// issue 模板：Playground 链接必填（缺链接 bot 自动关闭）
```
