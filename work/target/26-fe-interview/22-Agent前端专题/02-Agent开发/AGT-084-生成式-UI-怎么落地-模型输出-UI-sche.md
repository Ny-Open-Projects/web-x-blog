---
title: [AGT-084] 生成式 UI 怎么落地（模型输出 UI schema、前端渲染）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-084：生成式 UI 怎么落地（模型输出 UI schema、前端渲染）？
**答**：
- 生成式 UI：模型不输出 markdown 而输出 UI schema（组件类型 + props），模型负责「决定展示什么」，前端保证「怎么渲染是安全的」。
- 核心是组件注册表（白名单）：只有注册过的组件类型可渲染，props 先过 Zod 校验，未知类型或校验失败降级为文本卡片。
- schema 由后端 JSON Schema 约束模型输出；流式场景配合 partial JSON 渐进渲染（AGT-043）。
- 价值：图表/按钮/表单等交互组件可触发前端回调与后续工具调用，比纯文本表达力强得多。

```jsx
// 组件注册表 + schema 校验渲染
import { z } from 'zod';

const UISchema = z.object({
  components: z.array(z.object({ type: z.string(), props: z.record(z.unknown()) })),
});

const registry = {
  chart: {
    schema: z.object({ title: z.string(), data: z.array(z.object({ label: z.string(), value: z.number() })) }),
    render: (p) => <BarChart title={p.title} data={p.data} />,
  },
  table: {
    schema: z.object({ columns: z.array(z.string()), rows: z.array(z.array(z.string())) }),
    render: (p) => <DataTable columns={p.columns} rows={p.rows} />,
  },
  card: {
    schema: z.object({ title: z.string(), body: z.string() }),
    render: (p) => <InfoCard title={p.title} body={p.body} />,
  },
};

export function GenerativeUI({ modelOutput }) {
  const parsed = UISchema.safeParse(JSON.parse(extractJson(modelOutput)));
  if (!parsed.success) return <FallbackText text={modelOutput} />;    // 降级为纯文本
  return parsed.data.components.map((c, i) => {
    const comp = registry[c.type];
    if (!comp) return <FallbackText key={i} text={`不支持的组件 ${c.type}`} />;
    const props = comp.schema.safeParse(c.props);
    return props.success
      ? <div key={i}>{comp.render(props.data)}</div>
      : <FallbackText key={i} text="组件数据校验失败" />;
  });
}
```
