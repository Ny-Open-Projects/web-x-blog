---
title: [ENG-180] 团队 prompt 工程规范怎么定？结构 变量与评测怎么管理？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-180：团队 prompt 工程规范怎么定？结构 变量与评测怎么管理？
**答**：
- prompt 资产化管理：模板进仓库 .ai/prompts/，有版本有 owner有变更记录，与代码一样走 PR review。
- 结构规范五段式：角色 任务 上下文 约束 输出格式；变量统一 {{placeholder}}，禁止代码里散落 prompt 字符串。
- 评测配套：每个模板配评测集（输入样例 + 期望要点），模板改动跑评测对比通过率，防止改好 A 弄坏 B。
- 变量治理：注入内容做裁剪与脱敏，敏感字段不进 prompt。

```yaml
# .ai/prompts/component.md —— 组件生成 prompt 模板 五段式
role: 你是团队前端专家 熟悉 @corp/ui 组件库与 React 18
task: 根据需求描述生成一个 React 组件及其单测
context:
  props_types: "{{props_dts}}"
  similar_component: "{{reference_code}}"
constraints:
  - 使用函数组件与 hooks 不使用 class
  - 样式用 CSS Modules 前缀 {{style_prefix}}
  - 不引入新依赖 不修改 {{props_dts}} 之外的类型
output:
  format: 两个代码块 分别为 Component.tsx 与 Component.test.tsx
  language: typescript
# 评测集 evaluation/cases.yaml prompt 变更 CI 跑对比 通过率不低于基线
```
