---
title: [AGT-197] Agent 与低代码平台怎么结合（AI 生成低代码 schema 的闭环）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-197：Agent 与低代码平台怎么结合（AI 生成低代码 schema 的闭环）？
**答**：
- 结合点：低代码平台的 schema（页面/流程/数据模型 DSL）天然是「结构化、可校验、有 schema 约束」的——正好是 LLM 最擅长的生成目标，等于给 AI 生成加了一层「合法性护栏」。
- 闭环五步：自然语言 → LLM 生成 schema 草稿 → 平台校验器（schema 合法性 + 引用完整性 + 权限规则）→ 渲染预览 → 用户在可视化编辑器修正（修正 diff 回流为 few-shot 素材）。
- 质量关键：schema 生成要「渐进约束」——先让 LLM 选模板/布局（低自由度枚举），再填字段绑定（受数据模型约束），最后生成事件逻辑（受限表达式而非自由代码），自由度逐层放大，错误率逐层受控。
- 前端工程师的角色转变：从写页面到「设计可被 AI 填充的 schema 语言 + 校验器 + 修正体验」——DSL 的表达能力与 AI 生成成功率直接相关。

```typescript
// AI 生成低代码 schema 的校验与修正闭环
import { z } from 'zod';

const LcComponent = z.object({
  type: z.enum(['form', 'table', 'chart', 'button']),        // 低自由度：枚举模板
  props: z.record(z.unknown()),
  bindings: z.array(z.object({
    field: string4(),                                        // 必须引用已声明数据模型字段
    widget: z.enum(['input', 'select', 'date', 'number']),
  })).default([]),
  onEvent: z.object({ event: z.enum(['click', 'change']), action: string4() }).optional(), // 受限表达式
});
const LcSchema = z.object({
  page: string4(), dataModel: z.record(z.array(string4())),  // 数据模型：字段白名单
  components: z.array(LcComponent),
});
function string4() { return z.string(); }
type LcSchema = z.infer<typeof LcSchema>;

export async function aiGeneratePage(prompt: string, call: (p: string) => Promise<string>) {
  const raw = await call(`生成低代码页面 JSON，组件 type 只能是 form/table/chart/button，字段必须引用数据模型：\n${prompt}`);
  let schema: LcSchema;
  try {
    schema = LcSchema.parse(JSON.parse(raw));               // 第 1 层：schema 合法性
  } catch (e) {
    return repairLoop(prompt, raw, (e as Error).message, call);   // 校验失败回喂修复
  }
  const errors = validateReferences(schema);                // 第 2 层：引用完整性
  if (errors.length) return repairLoop(prompt, JSON.stringify(schema), errors.join('; '), call);
  return { schema, preview: renderPreview(schema) };        // 第 3 层：渲染预览交用户修正
}

function validateReferences(s: LcSchema): string[] {
  const errors: string[] = [];
  for (const c of s.components) {
    for (const b of c.bindings) {
      const fields = Object.values(s.dataModel).flat();
      if (!fields.includes(b.field)) errors.push(`组件绑定引用了不存在的字段：${b.field}`);
    }
  }
  return errors;
}
async function repairLoop(prompt: string, bad: string, error: string, call: (p: string) => Promise<string>) {
  const fixed = await call(`你的输出未通过校验：${error}\n原输出：${bad.slice(0, 1000)}\n请修正后重新输出。`);
  return { schema: LcSchema.parse(JSON.parse(fixed)), preview: renderPreview(LcSchema.parse(JSON.parse(fixed))) };
}
function renderPreview(s: LcSchema) { return `preview:${s.page}(${s.components.length} components)`; }
```
