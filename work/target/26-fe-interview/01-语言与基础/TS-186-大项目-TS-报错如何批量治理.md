---
title: [TS-186] 大项目 TS 报错如何批量治理？
date: 2026-11-17
categories: [TypeScript]
tags: [前端面试, 面试题, 05]
type: 面试题
---

## TS-186：大项目 TS 报错如何批量治理？
**答**：
- 基线冻结：现有错误总数入库，CI 只允许减少不允许新增。
- 工具约束：eslint ban-ts-comment 统一 @ts-expect-error（必须带描述，错误修复后该行自动报"未使用"，驱动清理）。
- 数据驱动：按目录统计错误数做看板，Owner 认领 + 趋势 review；分包开启 strict 逐包收口。

```typescript
// 1) 基线生成（CI 脚本伪代码）
// npx tsc --noEmit > ts-errors.txt
// 统计行数与分布，写入 ts-baseline.json；PR 中错误总数 > 基线则失败

// 2) eslint 约束注释滥用
// { "rules": { "@typescript-eslint/ban-ts-comment": ["error", {
//   "ts-ignore": "allow-with-description",
//   "ts-expect-error": "allow-with-description",
//   "minimumDescriptionLength": 10 }] } }

// 3) @ts-expect-error 的自愈特性：被压住的错误修复后，
// 该行反而报"Unused '@ts-expect-error' directive"，天然驱动清理

const x: number = "1"; // @ts-expect-error 演示占位：待迁移的遗留赋值
console.log(x);
```
