---
title: [ARC-188] 演进式架构原则与适应度函数（Fitness Function）如何落地？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-188：演进式架构原则与适应度函数（Fitness Function）如何落地？
**答**：
- 演进式架构核心思想：架构不是一次性设计而是持续约束，"适应度函数"把架构特征（耦合度、性能、安全、依赖方向）变成可自动执行的验证指标，进 CI 持续运行——架构守护从"人肉评审"变成"机器卡口"。
- 前端落地实例：依赖方向检查（ eslint import 规则：上层禁引下层实现）、包体积与性能预算（每次构建验证）、圈复杂度阈值、API 兼容性检测（公开导出 diff）、无障碍扫描达标率。
- 设计原则：适应度函数要可自动执行、结果可量化、劣化能报警；从团队最痛的架构特征开始（通常是依赖混乱与包体积），不要一次铺满。
- 与 ADR 联动：每条架构决策落地时回答"这个约束如何变成适应度函数"，决策才能长期生效而不是文档里的愿望。

```typescript
// 前端适应度函数示例（CI 中执行）
// fitness/dependency-direction.test.ts —— 架构特征：分层依赖方向
import { walk } from 'estree-walker';
import { glob } from 'glob';

const RULES = [
  { layer: 'apps/',    forbid: /^packages\/[^/]+\/src\/(internal|impl)\// },   // 应用禁引实现细节
  { layer: 'domains/', forbid: /^apps\// },                                    // 领域层禁依赖应用层
  { layer: 'base/',    forbid: /^(apps|domains)\// },                          // 基础层禁向上依赖
];

test('分层依赖方向符合架构约束', async () => {
  const violations: string[] = [];
  for (const file of await glob('{apps,domains,base}/**/*.{ts,tsx}', { ignore: ['**/*.test.ts'] })) {
    const imports = await extractImports(file);
    for (const imp of imports) {
      for (const rule of RULES) {
        if (file.startsWith(rule.layer) && rule.forbid.test(imp)) {
          violations.push(`${file} → ${imp} 违反分层规则 [${rule.layer}]`);
        }
      }
    }
  }
  // 适应度函数输出：违规数必须为 0（或 ≤ 存量豁免清单数且只减不增）
  expect(violations).toEqual([]);
});

// 其他适应度函数（同目录，CI 全量执行）：
// fitness/bundle-budget.test.ts      首屏 JS ≤ 300KB gzip
// fitness/api-compat.test.ts         公开导出 diff 无 breaking
// fitness/complexity.test.ts         圈复杂度 > 15 的函数数不增长
// 特性：可自动执行 / 可量化 / 劣化即红 —— 架构约束的"活体检验"
```
