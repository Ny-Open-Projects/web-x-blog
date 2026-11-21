---
title: [ENG-111] 代码所有权与依赖边界怎么用工具强制？dependency-cruiser 实战？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-111：代码所有权与依赖边界怎么用工具强制？dependency-cruiser 实战？
**答**：
- 所有权：CODEOWNERS 指定目录到 reviewer 的映射，PR 自动请求对应负责人审批。
- 边界：dependency-cruiser 扫描 import 关系，声明"谁不能依赖谁"（包间、分层间），违规即 CI 失败。
- 与 ESLint 分工：no-restricted-imports 适合单仓内分层；dependency-cruiser 适合跨包依赖图与循环依赖检测。
- 规则要渐进：存量违规先用 warn 观察并生成基线文件，新违规 error 卡死，避免一刀切导致门禁被绕过。

```javascript
// .dependency-cruiser.cjs
module.exports = {
  forbidden: [
    {
      name: 'ui 包不得依赖 apps',
      severity: 'error',
      from: { path: '^packages/ui' },
      to: { path: '^apps' },
    },
    {
      name: '禁止循环依赖',
      severity: 'error',
      from: {},
      to: { circular: true },
    },
  ],
};
// npx depcruise --validate .dependency-cruiser.cjs packages apps
```

```text
# CODEOWNERS：目录到 reviewer 的映射
/packages/ui/        @myorg/ui-team
/apps/web/           @myorg/web-team
/.github/workflows/  @myorg/infra-team
```

---

## 第二十四章 质量与度量（ENG-112 ~ ENG-117）
