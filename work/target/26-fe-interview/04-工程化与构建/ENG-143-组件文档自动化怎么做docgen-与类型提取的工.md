---
title: [ENG-143] 组件文档自动化怎么做？docgen 与类型提取的工程链路？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-143：组件文档自动化怎么做？docgen 与类型提取的工程链路？
**答**：
- 手写 props 文档必然漂移：从 TS 类型与 JSDoc 注释自动提取（react-docgen-typescript / vue-docgen-api），注释即文档。
- 提取结果生成三件套：props 表格、默认值、事件与插槽说明，挂进文档站组件详情页。
- JSDoc 质量要有卡口：@default、@deprecated、示例块是 docgen 的原料来源，lint 保证注释覆盖。
- 文档 diff 随组件版本发布：类型变更自动生成文档 PR，review 组件时连带审文档。

```typescript
// scripts/gen-component-docs.ts —— 从类型定义自动提取组件文档
import { parse } from 'react-docgen-typescript'
import { writeFileSync } from 'node:fs'

const results = parse('./src/components/**/*.tsx', {
  savePropValueAsString: true,
  shouldExtractValuesFromTag: true,
  propFilter: prop => !/node_modules/.test(prop.parent?.fileName ?? ''), // 过滤三方透传 props
})

for (const c of results) {
  const md = [
    `# ${c.displayName}`,
    c.description ?? '',
    '| 属性 | 类型 | 默认值 | 说明 |',
    '| --- | --- | --- | --- |',
    ...Object.values(c.props).map(p =>
      `| ${p.name} | \`${p.type.name}\` | ${p.defaultValue?.value ?? '-'} | ${p.description.split('\n')[0]} |`),
  ].join('\n')
  writeFileSync(`docs/components/${c.displayName}.md`, md)
}
```
