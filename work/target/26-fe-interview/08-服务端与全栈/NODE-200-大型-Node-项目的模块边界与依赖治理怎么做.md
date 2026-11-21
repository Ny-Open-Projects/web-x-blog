---
title: [NODE-200] 大型 Node 项目的模块边界与依赖治理怎么做？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-200：大型 Node 项目的模块边界与依赖治理怎么做？
**答**：
- 分层架构：routes（接口）→ services（领域）→ repos（数据）→ infra（外部客户端）；规则：上层可依赖下层，**禁止反向与跨层跳跃**。
- 自动化守护：eslint-plugin-boundaries 声明依赖方向，违反直接 lint 报错；madge 检测循环依赖，CI 阻断。
- 公共代码强制走 `@shared` 包（NODE-154 monorepo workspace），杜绝"顺手 import 别的模块内部文件"。
- 度量腐化：单文件行数/扇出/圈复杂度超阈值在 review 提示；治理看"腐化速度"而不只是现状。

```javascript
// .eslintrc.cjs —— eslint-plugin-boundaries 依赖方向约束
module.exports = {
  rules: {
    'boundaries/element-types': ['error', {
      default: 'disallow',
      rules: [
        { from: ['routes'], allow: ['service'] },
        { from: ['service'], allow: ['repo', 'service'] },
        { from: ['repo'], allow: ['infra'] },
        { from: ['infra'], allow: [] },              // 最底层不依赖业务层
      ],
    }],
  },
  settings: {
    'boundaries/elements': [
      { type: 'routes', pattern: 'src/routes/**' },
      { type: 'service', pattern: 'src/services/**' },
      { type: 'repo', pattern: 'src/repos/**' },
      { type: 'infra', pattern: 'src/infra/**' },
    ],
  },
};
// CI 循环依赖检测：npx madge --circular --extensions ts src → 有环则退出码 1
// 公共代码：import { x } from '@acme/shared'（workspace 包，NODE-154）
```
