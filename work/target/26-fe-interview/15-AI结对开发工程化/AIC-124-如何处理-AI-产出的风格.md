---
title: [AIC-124] 如何处理 AI 产出的风格不一致问题？「代码风格统一」在 AI 时代怎么治理？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-124：如何处理 AI 产出的风格不一致问题？「代码风格统一」在 AI 时代怎么治理？
**答**：
- 问题表现：不同工具/模型的产出风格混杂（分号、引号、组件写法、抽象风格）、同一文件被 AI 改得局部风格突变、AI 偏爱训练数据里的主流风格而非本仓库风格。
- 治理分层：可自动化的全交给工具链（Prettier/ESLint 强制，AI 违反也跑不掉）——风格治理的第一原则是「机器能管的绝不靠 prompt」。
- 工具管不了的语义风格：组件拆分粒度、错误处理模式、抽象层级——这些进规则文件 + few-shot 示例（AIC-026），并靠 review 清单兜底。
- 混杂修复：让 AI 自己当「风格统一器」——按本仓库 dominant style 重写指定文件（机械变换，验证方式与重构同 AIC-052）。
- 追问钩子：回答亮点是「风格治理的自动化率」——能用 lint/prettier 消灭的风格问题占比越高，规则文件越轻松。

```json
// .prettierrc：风格问题机器执法，不进 prompt
{ "semi": true, "singleQuote": true, "printWidth": 100 }
```
```text
语义风格进规则（规则文件片段）：
- 组件优先函数式 + hooks；禁止 class 组件
- 错误处理用 Result 型（see ai/knowledge/error-pattern.md）
- 新抽象必须先有第二个使用场景（防过度抽象）
```
