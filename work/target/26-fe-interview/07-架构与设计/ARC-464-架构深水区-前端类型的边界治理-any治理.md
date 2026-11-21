---
title: [ARC-464] 大型项目的 TypeScript 边界治理：any 治理与类型防线
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-464：TypeScript 边界治理：any 治理与类型防线
**答**:
- 类型防线分层：入口处强类型（接口响应 parse 成类型、路由参数 schema 化）、边界内类型流动（strict 模式 + noUncheckedIndexedAccess）、出口处窄化（对外导出类型明确，不暴露实现细节类型）。
- any 治理路径：先量化（any 数量/占比基线）、禁增量（lint: no-explicit-any error + 豁免清单）、存量收敛（any → unknown → 收窄；第三方无类型 → d.ts 声明或 @ts-expect-error 注明理由）。
- unknown 的正确用法：外部输入一律 unknown，先校验再使用——把"运行时类型检查"编码进类型系统（zod parse 的返回值类型）。
- 类型即契约：公共 API 的类型变更走 review（类型 diff 工具 api-extractor 报告 breaking change）；类型不参与运行时的误解要澄清——schema 才是运行时契约，类型是编译期投影。
- 收益度量：类型覆盖率（any/unknown 占比）、编译错误逃逸率（线上 typeof 相关错误归因）。
```typescript
// 入口强类型：unknown → schema 校验 → 类型流动
import { z } from 'zod';
const GoodsSchema = z.object({ id: z.string(), price: z.number() });
type Goods = z.infer<typeof GoodsSchema>;
async function getGoods(id: string): Promise<Goods> {
  const raw: unknown = await api(`/goods/${id}`);          // 外部输入 unknown
  return GoodsSchema.parse(raw);                            // 校验 + 收窄
}
```
