---
title: [ENG-179] AI 辅助重构怎么工程化？codemod 与 LLM 混合方案怎么设计？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-179：AI 辅助重构怎么工程化？codemod 与 LLM 混合方案怎么设计？
**答**：
- 分工明确：确定性变更（API 改名 import 调整 参数顺序）用 codemod 100% 可靠；语义性变更（class 组件改 hooks 拆组件）用 LLM 灵活但需验证。
- 流水线：codemod 先跑机械部分 → LLM 处理剩余难改文件 → 每文件改完即跑编译与关联单测，失败回滚该文件进人审清单。
- LLM 输出过 AST 校验：parse 失败或引入禁用 API 直接打回，不让语法垃圾进 review。
- 持续沉淀：统计两类工具成功率，把 LLM 已稳定处理的语义规则固化成新 codemod。

```javascript
// scripts/hybrid-refactor.mjs —— codemod 与 LLM 混合重构流水线
import { execSync } from 'node:child_process'
import { readFileSync, writeFileSync, appendFileSync } from 'node:fs'

// 1. 机械部分 codemod 全量执行
execSync('npx jscodeshift -t codemods/api-v2.ts src/ --extensions=ts,tsx')

// 2. 剩余含旧模式的文件交给 LLM 语义改写
const left = execSync("grep -rl 'this.setState' src/ --include='*.tsx' || true")
  .toString().split('\n').filter(Boolean)

for (const file of left) {
  const original = readFileSync(file, 'utf8')
  const rewritten = await llmRewrite(original, RULES_HOOK_STYLE)
  writeFileSync(file, rewritten)
  try {
    execSync('pnpm tsc --noEmit -p .')
    execSync(`pnpm vitest run related --file ${file}`)
  } catch {
    writeFileSync(file, original)               // 失败回滚单文件 进人审清单
    appendFileSync('refactor-manual-review.txt', `${file}\n`)
  }
}
```
