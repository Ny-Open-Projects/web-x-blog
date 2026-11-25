---
title: [RBL-262] 构建配置的 DSL 设计：约定优于配置怎么落地
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-262：构建配置的 DSL 设计：约定优于配置怎么落地

**答**:
- 约定先行：目录约定（src/entries、src/env）+ 命名约定（*.env.ts）→ 配置项大量消失；约定文档化且由脚手架强制（新文件放错位置直接报错）
- 配置收敛设计：暴露的配置面要「按场景」而非「按参数」——`output: 'spa' | 'lib' | 'mpa'` 一个选项展开成十几个底层参数；避免把引擎参数原样漏出
- 兜底逃生舱：任何约定都提供 raw 覆盖（tools.rspack 直改底层），但使用处登记（code review 检查项）——约定覆盖不了的长尾需求
- 演进纪律：配置项增减走 RFC；废弃配置保留一个版本的警告映射到新配置

```javascript
// 场景化配置展开
export default defineConfig({
  output: 'lib',      // → 展开为: format dual + dts + external peers + minify lib 预设
})
// 逃生舱
tools: { rspack: (cfg) => { cfg.resolve.alias = {...} } }   // 使用处需登记
```
