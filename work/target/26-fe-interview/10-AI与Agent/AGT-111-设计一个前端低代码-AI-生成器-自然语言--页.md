---
title: [AGT-111] 设计一个前端低代码 AI 生成器（自然语言 → 页面 schema）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-111：设计一个前端低代码 AI 生成器（自然语言 → 页面 schema）？
**答**：
- 自然语言 → 页面 schema（组件树 + props），前端渲染器把 schema 映射到低代码组件库——模型只产出受控 DSL，渲染永远安全。
- schema 设计是核心：组件类型白名单（enum）、props 用 Zod 约束、嵌套深度限制；schema 版本化以兼容历史页面。
- 交互闭环：生成 → 预览 → 用户点选组件追加修改指令（「把按钮改成红色」）→ 增量 patch schema 而非整体重生成（省 token 且保留用户手工调整）。
- 校验失败自动修复（复用 AGT-048），未知组件渲染占位，绝不让非法 schema 打崩编辑器。

```jsx
// 页面 schema 与渲染器
import { z } from 'zod';

const NodeSchema = z.object({
  type: z.enum(['section', 'heading', 'text', 'button', 'form', 'image']),
  props: z.record(z.unknown()),
  children: z.array(z.lazy(() => NodeSchema)).max(10).default([]),
});
const PageSchema = z.object({ page: z.object({ title: z.string(), children: z.array(NodeSchema).max(20) }) });

const RENDERERS = {
  heading: (p) => <h2 style={p.style}>{p.text}</h2>,
  text:    (p) => <p style={p.style}>{p.content}</p>,
  button:  (p) => <button style={p.style} onClick={p.onClick}>{p.label}</button>,
  form:    (p) => <form>{p.fields.map((f) => <input key={f.name} placeholder={f.label} />)}</form>,
  image:   (p) => <img src={p.src} alt={p.alt} />,
  section: (p) => <section style={p.style}>{p.children}</section>,
};

function renderNode(node, key = 0) {
  const R = RENDERERS[node.type];
  if (!R) return <Placeholder key={key} type={node.type} />;   // 未知类型兜底
  return <R key={key} {...node.props}>{node.children.map((c, i) => renderNode(c, i))}</R>;
}

export async function generatePage(prompt) {
  const schema = await structuredLLM(
    [{ role: 'user', content: `生成页面 schema，组件类型限 section/heading/text/button/form/image：\n${prompt}` }],
    PageSchema,
  );
  return schema; // 存库后由 renderNode 预览；后续修改走增量 patch
}
```
