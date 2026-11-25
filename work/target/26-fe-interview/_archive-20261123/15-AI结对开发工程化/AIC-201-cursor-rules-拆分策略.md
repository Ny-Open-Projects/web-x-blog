---
title: [AIC-201] 大型仓库的 Cursor rules 应该如何拆分与组织？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-201：大型仓库的 Cursor rules 应该如何拆分与组织？
**答**：
- 按「作用域」拆：仓库级（编码规范、架构约定）用 alwaysApply，模块级（components/api/hooks）用 glob 匹配，任务级（迁移、调试流程）按需 @ 引用。
- 单条规则控制在 100 行以内：长规则会被截断且稀释注意力，超过就拆成多条并交叉引用。
- 规则要版本化进 git、走 PR 评审，和代码同级对待；规则本身的变更要有 changelog。
- 避免规则冲突：同一文件命中多条规则时内容会拼接，冲突指令要设优先级或在规则内显式声明覆盖关系。

```javascript
// .cursor/rules 的目录化组织
// rules/
//   base.mdc          alwaysApply: true  → 仓库通用规范
//   components.mdc    globs: src/components/**/*.tsx
//   api-layer.mdc     globs: server/api/**/*.ts
//   migration-guide.mdc  description: 执行 DB 迁移任务时引用（agent 按语义匹配）
const ruleLayers = {
  always: ['base'],                 // 每次必注入，最稀缺，只放最核心约定
  glob: ['components', 'api-layer'], // 按文件路径注入，承载模块级约定
  agent: ['migration-guide'],        // 按任务语义注入，description 要写清触发场景
};
// 原则：always 最小化、glob 精确化、agent 描述化，三层总量 < 8k tokens
r
```
