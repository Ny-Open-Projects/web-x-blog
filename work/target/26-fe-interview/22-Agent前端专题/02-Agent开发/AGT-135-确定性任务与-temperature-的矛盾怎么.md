---
title: [AGT-135] 确定性任务与 temperature 的矛盾怎么处理？如何让 Agent 输出稳定可复现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-135：确定性任务与 temperature 的矛盾怎么处理？如何让 Agent 输出稳定可复现？
**答**：
- 矛盾本质：temperature=0 也不是严格确定（MoE 路由、浮点非结合性、批处理调度都会引入波动），且过低温度会让模型陷入重复——要靠「参数+结构+校验」组合拳而非单点温度。
- 组合拳：分类/抽取类任务用 temperature 0~0.2 + JSON schema 强约束 + few-shot 固定示例；生成类任务保留 0.7 左右但把「随机性」约束到风格层。
- 可复现三件套：固定 seed（支持的模型）、快照版模型（`gpt-4o-2024-11-20` 这类带日期版本，避免 silent 更新）、输入指纹（prompt 模板版本+参数哈希入 trace）。
- 最终兜底永远是运行时 schema 校验 + 失败重试，把「概率系统」包装出「确定性接口」。

```typescript
// 确定性任务的推理封装：低温 + seed + 版本快照 + 校验重试
import { z } from 'zod';

const ExtractResult = z.object({ intent: z.enum(['refund', 'consult', 'complaint']), orderNo: z.string().nullable() });

export async function deterministicExtract(text: string): Promise<z.infer<typeof ExtractResult>> {
  const body = {
    model: 'gpt-4o-2024-11-20',            // 快照版：拒绝静默升级
    temperature: 0,                        // 低温压随机性
    seed: 42,                              // 可复现（支持 seed 的模型）
    response_format: { type: 'json_object' },
    messages: [
      { role: 'system', content: '你是意图分类器。只输出 JSON，字段 intent 与 orderNo。' },
      { role: 'user', content: `文本：${text}\n输出 JSON：` },
    ],
  };
  const res = await fetch(`${process.env.OPENAI_BASE_URL}/chat/completions`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${process.env.OPENAI_API_KEY}` },
    body: JSON.stringify(body),
  }).then((r) => r.json());

  const raw = res.choices[0].message.content as string;
  const parsed = ExtractResult.safeParse(JSON.parse(raw));
  if (parsed.success) return parsed.data;
  throw new Error('结构化输出校验失败，进入重试队列'); // 兜底交给上层校验重试矩阵（见 AGT-138）
}
```
