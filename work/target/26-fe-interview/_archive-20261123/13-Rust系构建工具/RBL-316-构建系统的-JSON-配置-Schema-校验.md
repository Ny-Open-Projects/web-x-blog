---
title: [RBL-316] 构建系统的配置 Schema 校验怎么做
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-316：构建系统的配置 Schema 校验

**答**:
- 校验三层：结构（字段类型/必填）、语义（值域/依赖组合合法性——A 选项与 B 互斥）、环境（当前环境允许的值域）——构建 fail-fast 而不是运行时诡异行为
- Schema 来源：zod/json-schema 单一事实源 → 生成 TS 类型（config 类型自动同步）+ 生成文档（配置项列表自动更新）——类型/文档/校验三者同源
- 错误体验：违规配置给出「最接近的正确写法」建议（did you mean）+ 违规位置（配置文件行号）
- 演进保护：新增字段默认宽容（unknown 字段警告而非报错——向前兼容），删除字段走废弃周期

```javascript
const schema = z.object({
  output: z.enum(['spa', 'lib', 'mpa']),
  minify: z.boolean().default(true),
}).strict({ message: 'unknown option (did you mean minify?)' })
// zod schema → 生成 ts 类型 + 文档 + 构建期校验
```
