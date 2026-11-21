---
title: [AIC-037] 用中文还是英文写 Prompt 对代码生成质量有影响吗？团队规范该怎么定？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-037：用中文还是英文写 Prompt 对代码生成质量有影响吗？团队规范该怎么定？
**答**：
- 客观情况：主流模型的中英编码能力差距在缩小，但英文 prompt 在**token 效率**上仍占优（同样内容中文通常多 30%~50% token），长上下文任务下影响预算。
- 术语保真：技术名词（debounce、HOC、SSR）保持英文原词，夹杂翻译腔的中文术语反而增加歧义；代码标识符必须英文。
- 团队规范建议：需求描述用团队母语（中文）保证沟通准确度，约束清单和输出格式模板用英文关键字 + 中文说明混合；注释语言统一（和项目现状一致）。
- 别用 prompt 语言影响产物语言：显式声明「代码注释用英文/中文」，否则模型会跟随 prompt 语言随机选。
- 追问钩子：与其纠结语言，不如把高频需求做成双语模板——模板化之后语言差异基本被抹平。

```javascript
// 双语模板约定示例
const template = `
# Task (English keywords for precision)
Implement useDebouncedValue hook.

# 约束（中文，保证团队理解一致）
- TypeScript strict，禁止 any
- 副作用必须清理

# Output language
Code & identifiers: English. Comments: Chinese (简体中文).
`;
```
