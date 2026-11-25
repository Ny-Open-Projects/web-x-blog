---
title: [RBL-265] 构建工具的 Node API 与 CLI 双形态怎么设计
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-265：构建工具的 Node API 与 CLI 双形态怎么设计

**答**:
- 双形态价值：CLI 面向人（彩色输出/进度/flag），Node API 面向程序（CI 编排/测试集成/自定义脚本）——两者共享同一核心（CLI 是 API 的薄壳）
- 设计要点：API 返回结构化结果（stats/产物清单/错误对象），CLI 负责渲染；API 版本 semver 独立管理（API 是被依赖的接口，变更影响下游）
- 编程化场景：monorepo 编排器调用 API 拿产物清单做缓存 key；测试框架内嵌构建 API 做集成 fixture 构建
- 反模式：CLI 输出当 API 用（grep 终端文本解析）——脆弱；或 API 返回纯 log 字符串

```javascript
// Node API 形态
const { build } = require('tool')
const result = await build({ config })
// result: { stats: { time, assets: [{name, size}] }, errors: [] }
// CLI = parse args → build() → 渲染 result
```
