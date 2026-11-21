---
title: [ENG-178] 内部组件库的 AI 文档与示例生成怎么做？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-178：内部组件库的 AI 文档与示例生成怎么做？
**答**：
- 痛点是示例陈旧：AI 流水线从 props 类型与用法注释生成示例与文档，组件更新自动重建。
- 生成内容分层：基本用法确定性生成（类型驱动）、进阶组合示例 LLM 生成 + 沙箱可运行校验、FAQ 从高频 issue 生成候选。
- 质量卡口：生成的示例必须能在 vite 沙箱编译运行，跑不过不进文档站。
- 示例进 playground 可交互：AI 生成初始态，用户改 props 看效果并可导出代码。

```javascript
// scripts/gen-examples.mjs —— AI 生成组件示例并沙箱校验
import { generate } from './llm-client.mjs'
import { parse } from 'react-docgen-typescript'
import { writeFileSync } from 'node:fs'

for (const comp of parse('src/components/**/*.tsx')) {
  const example = await generate({
    model: 'corp-llm-mini',                        // 成本分层 简单示例用小模型
    prompt: `为组件 ${comp.displayName} 生成一个最小可用示例 只用已声明的 props
输出单个 tsx 文件 不得引入新依赖
props: ${JSON.stringify(Object.keys(comp.props))}`,
  })
  const ok = await buildInSandbox(example)         // vite 沙箱编译校验
  if (ok) writeFileSync(`docs/examples/${comp.displayName}.tsx`, example)
  else console.warn(`skip ${comp.displayName} 示例编译失败 不进文档`)
}
```
