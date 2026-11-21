---
title: [ENG-176] 仓库级上下文工具怎么做？codebase 索引与检索增强的开发工具？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-176：仓库级上下文工具怎么做？codebase 索引与检索增强的开发工具？
**答**：
- LLM 不了解内部框架与领域约定：仓库级上下文工具把代码库建索引（AST 切分 + embedding + 向量库），检索增强回答"我们项目怎么写请求封装"。
- 流水线：函数级 AST 切分保住语义完整 → 批量 embedding → 向量库 upsert → IDE 插件/CLI 检索入口。
- 质量关键：索引随代码增量更新、内部术语表单独喂给模型、相似实现作为 few-shot 注入。
- 效果评估：维护内部问答基准集，索引策略调整跑基准对比，不凭感觉调参。

```typescript
// scripts/codebase-index.ts —— 仓库级索引流水线（骨架）
import { glob } from 'glob'
import { parse } from '@babel/parser'
import { readFileSync } from 'node:fs'

interface Chunk { path: string; symbol: string; code: string }

async function chunkRepo(): Promise<Chunk[]> {
  const files = await glob('src/**/*.{ts,tsx}', { ignore: ['**/*.test.*'] })
  const chunks: Chunk[] = []
  for (const f of files) {
    const code = readFileSync(f, 'utf8')
    const ast = parse(code, { sourceType: 'module', plugins: ['typescript', 'jsx'] })
    for (const node of ast.program.body) {          // AST 函数级切分 保住语义完整
      const name = (node as any).id?.name
      if (name || node.type === 'ExportDefaultDeclaration') {
        chunks.push({ path: f, symbol: name ?? 'default', code })
      }
    }
  }
  return chunks
}

// 后续步骤（伪码）
// const vectors = await embed(chunks.map(c => c.code))
// await vectorDB.upsert(chunks.map((c, i) => ({ id: `${c.path}#${c.symbol}`, values: vectors[i] })))
// 检索时语义 + 符号双路召回 上下文注入 prompt
```
