---
title: [ENG-219] 工程规范（ESLint/TS config）的统一与例外治理怎么做？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-219：工程规范统一与例外治理怎么做？
**答**：
- 配置单源：共享 eslint-config/tsconfig base 包（monorepo 内 `@org/eslint-config`），项目只 extends——配置升级一处生效，规则评审集中在配置包 PR。
- 例外治理：禁 inline disable 滥用——eslint-disable 必须带原因注释 + CI 统计 disable 密度（超标告警）；历史代码例外用 overrides 按目录声明（显式可枚举）而非逐行禁用。
- 规则升级节奏：新规则先 warn 两周（产出违规报告）→ 评审豁免清单 → 转 error——直接 error 会引发大量 disable 反弹。
- 规则有效性评审：每季度看「该规则拦住的问题数 vs 误报数」，误报高的规则降级或删除。
- 追问钩子：为什么「disable 要带原因 + 密度统计」——不带原因的 disable 是规则失效的黑洞（没人知道为什么禁、还能不能修）；密度统计让「规则绕过」成为可见指标而非暗坑。

```javascript
// @org/eslint-config/index.js —— 配置单源
module.exports = { extends: ['@org/base', '@org/react'],
  rules: { 'no-console': 'error', '@typescript-eslint/no-explicit-any': 'warn' } };
// 例外目录显式声明（可枚举）
module.exports.overrides = [{
  files: ['legacy/**'], rules: { 'no-console': 'off' } }];
// CI disable 密度
const density = countEslintDisable() / totalLines();
if (density > 0.01) fail(`eslint-disable 密度超标: ${density}`);
```
