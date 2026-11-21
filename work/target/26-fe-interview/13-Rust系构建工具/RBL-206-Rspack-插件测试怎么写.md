---
title: [RBL-206] Rspack 插件的测试怎么写
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-206：Rspack 插件的测试怎么写

**答**:
- 三层：单元测试（插件内纯逻辑，如 diff/转换函数直接测）、集成测试（真实 rspack 构建小 fixture 工程，断言产物内容）、快照测试（产物 hash/结构快照，防行为漂移）
- 集成测试模式：`rspack({ entry, plugins: [MyPlugin], output: { path: tmpdir } }).run(cb)`，然后读 tmpdir 产物断言
- fixture 工程：每个测试场景一个最小目录（1-3 个文件），构建要快（秒级）才能进 CI
- 异步钩子的插件用 `compiler.hooks.done` 收尾断言；带 emit 修改的断言产物文本含预期标记

```javascript
import { rspack } from '@rspack/core'
import path from 'node:path'

test('banner plugin injects comment', async () => {
  const out = path.join(__dirname, 'tmp-out')
  await new Promise((resolve, reject) => {
    rspack({
      entry: './fixtures/entry.js',
      output: { path: out },
      plugins: [new BannerPlugin()],
    }, (err, stats) => err ? reject(err) : resolve(stats))
  })
  const code = fs.readFileSync(path.join(out, 'main.js'), 'utf8')
  expect(code.startsWith('/*! build:')).toBe(true)
})
```
